from __future__ import annotations

import re
from typing import List

# Regex pattern used in the book for basic token splitting
DEFAULT_TOKEN_PATTERN = r"([,.:;?_!\"()\']|--|\s)"


def basic_tokenize(text: str, pattern: str = DEFAULT_TOKEN_PATTERN) -> List[str]:
    """
    Tokenize text by splitting on punctuation and whitespace, while keeping delimiters.
    Then strips and filters empty tokens.
    """
    parts = re.split(pattern, text)
    tokens = [p.strip() for p in parts if p and p.strip()]
    return tokens


def demo_regex_splits() -> None:
    text1 = "Hello, world. This, is a test."
    result1 = re.split(r"(\s)", text1)
    print("Demo 1 split:", result1)

    text2 = "Hello, world. Is this-- a test?"
    result2 = re.split(DEFAULT_TOKEN_PATTERN, text2)
    result2 = [item.strip() for item in result2 if item.strip()]
    print("Demo 2 split:", result2)
