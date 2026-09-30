"""Check the narrated section of a digital-news Markdown script."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


MIN_CHARS = 1250
MAX_CHARS = 1490
CHARS_PER_SECOND = 8.3


def narrated_text(markdown: str) -> str:
    match = re.search(
        r"^## 낭독 대본\s*$\n(?P<body>.*?)(?=^## 사실표\s*$)",
        markdown,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ValueError("'## 낭독 대본'과 '## 사실표' 구간을 찾지 못했습니다.")

    lines = []
    for line in match.group("body").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("[") and stripped.endswith("]"):
            continue
        lines.append(stripped)
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("script", type=Path)
    args = parser.parse_args()

    text = narrated_text(args.script.read_text(encoding="utf-8"))
    characters = len(text)
    estimated_seconds = round(characters / CHARS_PER_SECOND)
    result = {
        "file": str(args.script.resolve()),
        "characters_including_spaces": characters,
        "estimated_seconds": estimated_seconds,
        "question_sentences": text.count("?"),
        "character_range": [MIN_CHARS, MAX_CHARS],
        "time_range_seconds": [150, 180],
        "pass": MIN_CHARS <= characters <= MAX_CHARS
        and 150 <= estimated_seconds <= 180,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
