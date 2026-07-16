"""Storage manager for configuration and state persistence."""

import json
import os
import re
import shutil
from pathlib import Path
from typing import Any, Optional

from pydantic import ValidationError

from .._file_utils import _atomic_write_text
from ..models import Config


# Matches ${VAR_NAME} in string config values. Names follow env-var rules
# (ASCII letters, digits, underscore; must not start with a digit).
_ENV_VAR_PATTERN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}")


def safe_output_path(root: Path, filename: str) -> Path:
    """Return an output path only when it resolves below root."""
    resolved_root = root.resolve()
    candidate = (resolved_root / filename).resolve()
    if candidate.parent != resolved_root:
        raise ValueError(f"Output path escapes intended root: {candidate}")
    return candidate


def _expand_env_vars(value: Any) -> Any:
    """Recursively expand ``${VAR}`` references inside any string leaves.

    Containers (dicts, lists, tuples) are walked; non-string leaves are
    returned unchanged. Strings with no ``${...}`` tokens are returned
    unchanged. References to unset variables are **left as-is**, so
    ``${MISSING}`` round-trips to ``${MISSING}`` and surfaces as a clear
    downstream error rather than a silent empty string.

    This is intentionally identical to the behaviour ``RSSScraper`` uses
    for RSS feed URLs, so a single ``${VAR}`` convention works everywhere
    in the config (AI ``base_url``, feed URLs, webhook URLs, ...).
    """
    if isinstance(value, str):
        return _ENV_VAR_PATTERN.sub(
            lambda m: os.environ.get(m.group(1), m.group(0)),
            value,
        )
    if isinstance(value, dict):
        return {k: _expand_env_vars(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_expand_env_vars(v) for v in value]
    if isinstance(value, tuple):
        return tuple(_expand_env_vars(v) for v in value)
    return value


class ConfigError(ValueError):
    """Raised when configuration is missing or invalid."""

    pass


class StorageManager:
    """Manages file-based storage for configuration and state."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.config_path = self.data_dir / "config.json"
        self.summaries_dir = self.data_dir / "summaries"

        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.summaries_dir.mkdir(parents=True, exist_ok=True)

    def load_config(self) -> Config:
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}\n"
                f"Please create it based on the template in README.md"
            )

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ConfigError(
                f"Invalid JSON in configuration file: {self.config_path}\n" f"Error: {e}"
            ) from e

        # Expand ${VAR} references in every string value before pydantic
        # validation. Keeps credentials / private endpoints / tenant IDs
        # out of the JSON file so it is safe to commit to a public repo.
        data = _expand_env_vars(data)

        try:
            return Config.model_validate(data)
        except ValidationError as e:
            raise ConfigError(
                f"Configuration validation failed for {self.config_path}\n"
                f"Details: {e}"
            ) from e

    def save_config(self, config: Config, backup: bool = True) -> Path:
        """Save configuration to config.json, optionally backing up the existing file.

        Args:
            config: The Config object to save.
            backup: If True and config.json exists, copy it to config.json.bak first.

        Returns:
            Path to the saved config file.
        """
        if backup and self.config_path.exists():
            shutil.copy2(self.config_path, self.config_path.with_suffix(".json.bak"))

        content = json.dumps(
            config.model_dump(mode="json"), indent=2, ensure_ascii=False
        )
        _atomic_write_text(self.config_path, f"{content}\n")

        return self.config_path

    def save_daily_summary(
        self,
        date: str,
        markdown: str,
        language: str = "en",
        edition: Optional[str] = None,
    ) -> Path:
        edition_part = f"-{edition}" if edition else ""
        filename = f"ai-gold-{date}{edition_part}-{language}.md"
        filepath = safe_output_path(self.summaries_dir, filename)

        _atomic_write_text(filepath, markdown)

        return filepath

    def save_project_archive(self, items: list, date: str) -> int:
        """Write one markdown archive page per item to docs/_projects/.

        Returns the number of pages written. Each page carries front matter
        for Jekyll so it renders on GitHub Pages. The slug combines a short
        date stamp with a sanitized title so same-named projects on
        different days do not collide.
        """
        from datetime import datetime, timezone

        projects_dir = Path("docs/_projects")
        projects_dir.mkdir(parents=True, exist_ok=True)

        written = 0
        seen_slugs: set[str] = set()
        seen_urls: set[str] = set()

        for item in items:
            item_url = str(getattr(item, "url", "") or "")
            if item_url and item_url in seen_urls:
                continue
            if item_url:
                seen_urls.add(item_url)

            title = (item.title or "untitled").strip()
            base_slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", title).strip("-").lower()
            if not base_slug:
                base_slug = "project"
            slug = f"{date}-{base_slug}"
            if slug in seen_slugs:
                slug = f"{slug}-{written + 1}"
            seen_slugs.add(slug)

            published = getattr(item, "published_at", None)
            published_str = (
                published.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                if published
                else date
            )

            tags = ", ".join(getattr(item, "ai_tags", []) or [])
            score = getattr(item, "ai_score", None)
            score_str = f"{score:.1f}" if isinstance(score, (int, float)) else ""

            source_type = getattr(item, "source_type", None)
            source_name = getattr(source_type, "value", str(source_type)) if source_type else ""
            category = (item.metadata or {}).get("category", "") or ""

            stars = (item.metadata or {}).get("stars", "")
            stars_str = str(stars) if stars else ""
            repo_full = (item.metadata or {}).get("repo", "") or ""

            meta = item.metadata or {}
            ai_summary = getattr(item, "ai_summary", "") or ""

            # Enrichment fields (title_zh/detailed_summary_zh/background_zh/
            # community_discussion_zh) are populated by ContentEnricher in the
            # 2nd AI pass; fall back to ai_summary when enrichment failed.
            title_zh = meta.get("title_zh") or ""
            detailed_zh = meta.get("detailed_summary_zh") or ""
            background_zh = meta.get("background_zh") or ""
            discussion_zh = meta.get("community_discussion_zh") or ""
            sources = meta.get("sources") or []

            display_title = title_zh or title
            card_summary_raw = detailed_zh or ai_summary
            card_summary_flat = " ".join(card_summary_raw.split())

            meta_lines = []
            if source_name:
                meta_lines.append(f"source: {source_name}")
            if category:
                meta_lines.append(f"category: {category}")
            if score_str:
                meta_lines.append(f"ai_score: {score_str}")
            if stars_str:
                meta_lines.append(f"stars: {stars_str}")
            if repo_full:
                meta_lines.append(f"repo: \"{repo_full}\"")
            if card_summary_flat:
                escaped_summary = card_summary_flat.replace('"', '\\"')
                meta_lines.append(f"summary: \"{escaped_summary}\"")
            if tags:
                meta_lines.append(f"tags: \"{tags}\"")
            meta_block = "\n".join(meta_lines)
            meta_section = meta_block + "\n" if meta_block else ""

            url = getattr(item, "url", "")
            url_str = str(url) if url else ""

            author = getattr(item, "author", "") or ""

            body_parts = [f"# {display_title}\n", ""]

            if card_summary_flat:
                intro = card_summary_flat[:200]
                body_parts.append(f"> {intro}\n")
                body_parts.append("")

            meta_info = []
            if url_str:
                meta_info.append(f"**项目链接**：{url_str}")
            if author:
                meta_info.append(f"**作者**：{author}")
            if published:
                meta_info.append(f"**发布时间**：{published_str}")
            meta_info.append(f"**挖掘日期**：{date}")
            if score_str:
                meta_info.append(f"**AI 评分**：{score_str}/10")
            if stars_str:
                meta_info.append(f"**Star 数**：{stars_str}")
            if source_name:
                meta_info.append(f"**来源**：{source_name}")
            if tags:
                meta_info.append(f"**标签**：{tags}")
            if meta_info:
                body_parts.append("\n".join(meta_info) + "\n")
                body_parts.append("")

            if detailed_zh:
                body_parts.append("## 📌 项目详解\n")
                body_parts.append(detailed_zh + "\n")
                body_parts.append("")
            if background_zh:
                body_parts.append("## 🌐 背景与生态\n")
                body_parts.append(background_zh + "\n")
                body_parts.append("")
            if discussion_zh:
                body_parts.append("## 💬 社区讨论\n")
                body_parts.append(discussion_zh + "\n")
                body_parts.append("")

            if sources:
                body_parts.append("## 📚 参考链接\n")
                for src in sources:
                    src_url = src.get("url", "")
                    src_title = src.get("title", src_url) or src_url
                    if src_url:
                        body_parts.append(f"- [{src_title}]({src_url})")
                body_parts.append("")

            content = getattr(item, "content", "") or ""
            if content:
                body_parts.append("<details><summary>📄 查看原文内容</summary>\n")
                body_parts.append("")
                body_parts.append(content)
                body_parts.append("")
                body_parts.append("</details>\n")

            body = "\n".join(body_parts)

            discovered_date_prefix = f"{date}T12:00:00+00:00"
            escaped_title = display_title.replace('"', '\\"')
            front_matter = (
                "---\n"
                "layout: default\n"
                f"title: \"{escaped_title}\"\n"
                f"date: {discovered_date_prefix}\n"
                f"discovered_date: {date}\n"
                f"slug: {slug}\n"
                + meta_section
                + "---\n\n"
            )

            filepath = projects_dir / f"{slug}.md"
            _atomic_write_text(filepath, front_matter + body)
            written += 1

        return written

    def load_subscribers(self) -> list:
        """Loads the list of email subscribers."""
        subscribers_path = self.data_dir / "subscribers.json"
        if not subscribers_path.exists():
            return []

        try:
            with open(subscribers_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def add_subscriber(self, email_addr: str):
        """Adds a new subscriber email."""
        subscribers = self.load_subscribers()
        if email_addr not in subscribers:
            subscribers.append(email_addr)
            self._save_subscribers(subscribers)

    def remove_subscriber(self, email_addr: str):
        """Removes a subscriber email."""
        subscribers = self.load_subscribers()
        if email_addr in subscribers:
            subscribers.remove(email_addr)
            self._save_subscribers(subscribers)

    def _save_subscribers(self, subscribers: list):
        """Helper to save subscribers list."""
        subscribers_path = self.data_dir / "subscribers.json"
        _atomic_write_text(subscribers_path, json.dumps(subscribers, indent=2))
