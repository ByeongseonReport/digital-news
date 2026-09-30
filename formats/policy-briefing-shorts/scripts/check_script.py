"""Check the narrated section of a policy-briefing shorts Markdown script."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


MIN_CHARS = 850
MAX_CHARS = 1100
MIN_PARAGRAPHS = 13
MAX_PARAGRAPHS = 17
CHARS_PER_SECOND = 8.3


def narrated_paragraphs(markdown: str) -> list[str]:
    match = re.search(
        r"^### ① 쇼츠 대본\s*$\n(?P<body>.*?)(?=^### ② 커뮤니티 게시물\s*$)",
        markdown,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ValueError("'### ① 쇼츠 대본'과 '### ② 커뮤니티 게시물' 구간을 찾지 못했습니다.")

    paragraphs = []
    for block in re.split(r"\n\s*\n", match.group("body")):
        text = re.sub(r"\s+", " ", block.strip())
        if not text or text.startswith("**") or (text.startswith("[") and text.endswith("]")):
            continue
        paragraphs.append(text)
    return paragraphs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("script", type=Path)
    args = parser.parse_args()

    paragraphs = narrated_paragraphs(args.script.read_text(encoding="utf-8"))
    text = " ".join(paragraphs)
    characters = len(text)
    estimated_seconds = round(characters / CHARS_PER_SECOND)
    paragraph_count = len(paragraphs)
    result = {
        "file": str(args.script.resolve()),
        "characters_including_spaces": characters,
        "estimated_seconds": estimated_seconds,
        "paragraphs": paragraph_count,
        "character_range": [MIN_CHARS, MAX_CHARS],
        "time_range_seconds": [90, 120],
        "paragraph_range": [MIN_PARAGRAPHS, MAX_PARAGRAPHS],
        "pass": MIN_CHARS <= characters <= MAX_CHARS
        and 90 <= estimated_seconds <= 120
        and MIN_PARAGRAPHS <= paragraph_count <= MAX_PARAGRAPHS,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
