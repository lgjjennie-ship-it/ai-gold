"""GitHub Search API scraper - discovers trending AI repositories."""

import logging
import os
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType


logger = logging.getLogger(__name__)


class GitHubSearchScraper(BaseScraper):
    """Scraper using GitHub Search API to find trending repositories.

    Runs one query per configured ``query`` string and emits one ContentItem
    per repository hit. Uses ``GITHUB_TOKEN`` when available (Actions built-in
    token raises the rate limit from 10 to 30 req/min).
    """

    BASE_URL = "https://api.github.com"

    def __init__(self, config: "GitHubSearchConfig", http_client: httpx.AsyncClient):
        super().__init__({"config": config}, http_client)
        self.cfg = config
        self.token = os.getenv("GITHUB_TOKEN")

    def _get_headers(self) -> dict:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "AI-Gold-Aggregator",
        }
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        return headers

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.cfg.enabled:
            return []

        items: List[ContentItem] = []
        for query in self.cfg.queries:
            try:
                page_items = await self._fetch_query(query, since)
                items.extend(page_items)
            except Exception as e:
                logger.warning("GitHub search query '%s' failed: %s", query, e)
        return items

    async def _fetch_query(self, query: str, since: datetime) -> List[ContentItem]:
        results: List[ContentItem] = []
        per_page = min(self.cfg.per_page, 30)
        url = (
            f"{self.BASE_URL}/search/repositories"
            f"?q={query}&sort={self.cfg.sort}&order={self.cfg.order}"
            f"&per_page={per_page}"
        )

        response = await self.client.get(
            url, headers=self._get_headers(), follow_redirects=True
        )
        if response.status_code != 200:
            logger.warning(
                "GitHub search HTTP %s for query '%s': %s",
                response.status_code,
                query,
                response.text[:200],
            )
            return results

        data = response.json()
        for repo in data.get("items", [])[: self.cfg.per_page]:
            item = self._parse_repo(repo, query)
            if item:
                results.append(item)
        return results

    def _parse_repo(self, repo: dict, query: str) -> Optional[ContentItem]:
        repo_id = repo.get("id")
        if repo_id is None:
            return None

        full_name = repo.get("full_name", "")
        html_url = repo.get("html_url", "")
        description = repo.get("description") or ""
        stars = repo.get("stargazers_count", 0)
        language = repo.get("language") or ""
        topics = repo.get("topics", []) or []
        created = repo.get("created_at", "")
        pushed = repo.get("pushed_at", "")
        owner = (repo.get("owner") or {}).get("login", "")
        forks = repo.get("forks_count", 0)
        open_issues = repo.get("open_issues_count", 0)

        published_str = pushed or created
        try:
            published_at = datetime.fromisoformat(
                published_str.replace("Z", "+00:00")
            )
        except (ValueError, TypeError):
            published_at = datetime.now(timezone.utc)

        title = f"{full_name}  ★{stars}"
        content_parts = [
            f"{description}",
            "",
            f"Language: {language}",
            f"Stars: {stars}  Forks: {forks}  Open Issues: {open_issues}",
            f"Topics: {', '.join(topics) if topics else '(none)'}",
            f"Owner: {owner}",
            f"Created: {created}   Last Push: {pushed}",
        ]
        content = "\n".join(content_parts)

        return ContentItem(
            id=self._generate_id("github_search", "repo", str(repo_id)),
            source_type=SourceType.GITHUB,
            title=title,
            url=html_url,
            content=content,
            author=owner,
            published_at=published_at,
            metadata={
                "query": query,
                "repo": full_name,
                "stars": stars,
                "forks": forks,
                "language": language,
                "topics": topics,
                "category": self.cfg.category,
                "open_issues": open_issues,
            },
        )
