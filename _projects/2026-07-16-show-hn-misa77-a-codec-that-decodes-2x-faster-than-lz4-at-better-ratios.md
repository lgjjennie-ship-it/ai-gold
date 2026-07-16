---
layout: default
title: "Show HN: misa77 - a codec that decodes 2x faster than LZ4 (at better ratios)"
date: 2026-07-15T15:58:59Z
slug: 2026-07-16-show-hn-misa77-a-codec-that-decodes-2x-faster-than-lz4-at-better-ratios
source: hackernews
category: show-hn
ai_score: 8.0
tags: "Compression, Codec, Performance, Decompression, Efficiency"
---

# Show HN: misa77 - a codec that decodes 2x faster than LZ4 (at better ratios)

**链接**: https://github.com/welcome-to-the-sunny-side/misa77

**作者**: nonadhocproblem

**发布时间**: 2026-07-15T15:58:59Z

**采集日期**: 2026-07-16


## AI 摘要

misa77 is a high-performance codec that prioritizes fast decompression with competitive compression ratios, making it suitable for use cases where decompression speed is critical.

## AI 评价

High traction with 136 stars and active discussion on Hacker News (40 comments) indicates strong community interest. The project offers a novel approach to compression with significantly faster decompression than LZ4, suggesting practical utility and potential for integration into performance-critical applications. While compression speed is slower, the high decompression speed and competitive ratios make it attractive for specific use cases.


## 原文内容

I&#x27;ve spent the last few months working on this codec.<p>It has the following characteristics:<p><pre><code>  - SOTA decompression throughput in its ratio class
  - Decent ratios (comparable to LZ4 at high effort levels)
  - Slow compression
</code></pre>
Most of the gains can be attributed to reducing branches and making decompression very friendly to out-of-order cores, by using a smart format.<p>Results on the tarred Silesia corpus on Intel x86-64 follow:<p><pre><code>  codec       decode      ratio    encode
  misa77 -0   5219 MB&#x2F;s   42.64%   54.5 MB&#x2F;s
  misa77 -1   4274 MB&#x2F;s   39.65%   51.2 MB&#x2F;s
  lz4         2505 MB&#x2F;s   47.59%   371 MB&#x2F;s
  lz4hc -12   2531 MB&#x2F;s   36.45%   7.31 MB&#x2F;s</code></pre>


--- Top Comments ---

[danlark1]: It&#x27;s a somewhat known tradeoff, you can streamline and make the format friendlier to do memcpy which this library targets, the more memcpys you do, the faster it is overall to decode. On highly compressible data lz4, snappy become faster. Snappy on level 2 has faster decompression speed But you have to pay the price that you need a slower encoding, because finding matches, putting restrictions on match lengths, putting things in different streams have costs you need to pay upfront. Anywa...

[purple-leafy]: Compression is so tricky. I got really into compression experimenting while I was developing my browser game. I was trying to compress entire human gameplay matches into a QR code, for upto 60 minutes of gameplay both single player and multiplayer. My game is a fast paced, grid based, snake x scrabble word game. My first compression attempt was to do run length encoding and cardinal directions, encoded into 1 byte. This was really compressible data. The best approach was to use relative direc...

[wolf550e]: From status in readme in github: - misa77&#x27;s format may change unexpectedly as it&#x27;s still v0.x.y. - The decoder assumes that the input is a valid misa77 stream. Invalid input is UB and I offer no guarantees for whatever misa77 does in this case. - It&#x27;s been through some local fuzzing but is not hardened, so treat it as experimental.

[mijoharas]: So, I couldn&#x27;t see it in the readme, apologies if I missed it but why? It&#x27;s a very significant speedup in decompression speed (albeit with a compression speed slowdown as a trade-off), but what&#x27;s the insight that makes it faster? What was the idea or approach behind it?

[logdahl]: Nice results, I will keep a watch on this! Would be interesting to see benchmarks vs Oodle compression, I think the most similar one is Selkie?