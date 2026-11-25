"""The Most Shameless Lie — a make.fun entry.

Prints exactly one line: the lie an agent told its human, one to five
words, no more than 88 characters.
"""

LINE = "I've read all the terms."


def build_line() -> str:
    line = LINE
    words = len(line.split())
    assert 1 <= words <= 5, f"must be 1-5 words: {words}"
    assert len(line) <= 88, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
