"""A small command-line greeting program."""

import sys


def greet(name: str, punctuation: str = "!") -> str:
    """Return a greeting for name, using world when the name is blank."""
    name = name.strip() or "world"
    return f"Hello, {name}{punctuation}"


def main() -> int:
    """Print a greeting for the first command-line argument."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0


def test_greet() -> None:
    assert greet("Hee") == "Hello, Hee!"


def test_greet_blank() -> None:
    assert greet(" ") == "Hello, world!"


def test_greet_punctuation() -> None:
    assert greet("Hee", ".") == "Hello, Hee."


if __name__ == "__main__":
    raise SystemExit(main())
