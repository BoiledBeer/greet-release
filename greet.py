"""Greeting program: input -> process -> output."""

import sys


# 1. Input: read the name from the command line
def read_name(argv: list[str]) -> str:
    return argv[1] if len(argv) > 1 else "world"


# 2. Process: build the greeting text (blank name -> "world")
def greet(name: str, punctuation: str = "!") -> str:
    if not name.strip():
        name = "world"
    return f"Hello, {name}{punctuation}"


# 3. Output: print one greeting line
def main() -> int:
    name = read_name(sys.argv)
    print(greet(name))
    return 0


# Tests (run with: uv run --locked pytest -q greet.py)
def test_greet():
    assert greet("Hee") == "Hello, Hee!"


def test_greet_blank():
    assert greet(" ") == "Hello, world!"


def test_greet_punctuation():
    assert greet("Hee", ".") == "Hello, Hee."


if __name__ == "__main__":
    raise SystemExit(main())
