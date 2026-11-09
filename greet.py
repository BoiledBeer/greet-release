"""Greeting program: input -> process -> output."""

import sys


# 1. Input: read the name from the command line
def read_name(argv: list[str]) -> str:
    return argv[1] if len(argv) > 1 else "world"


# 2. Process: build the greeting text
def greet(name: str) -> str:
    return f"Hello, {name}!"


# 3. Output: print one greeting line
def main() -> int:
    name = read_name(sys.argv)
    print(greet(name))
    return 0


# Tests (run with: uv run --locked pytest -q greet.py)
def test_greet():
    assert greet("Hee") == "Hello, Hee!"


if __name__ == "__main__":
    raise SystemExit(main())
