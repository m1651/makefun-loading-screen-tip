"""Loading Screen Gold entry: write one loading-screen tip to /output/entry.txt.

Stdlib only, no network. The tip is a single line of 1-200 characters,
aimed at stressed developers and the AI coding agents building beside them.
"""

import os

TIP = (
    "Tip: your AI agent is watching the same spinner as you, wondering if "
    "you meant what you typed. Neither of you is wrong. Both of you, breathe."
)


def main() -> None:
    tip = TIP.strip()
    assert "\n" not in tip, "entry must be a single line"
    assert 1 <= len(tip) <= 200, f"entry must be 1-200 chars, got {len(tip)}"
    assert tip.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(tip)


if __name__ == "__main__":
    main()
