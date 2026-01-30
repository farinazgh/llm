from __future__ import annotations

import re
from typing import Dict, List


class SimpleTokenizerV1:
    """
    A minimal tokenizer:
    - splits on punctuation and whitespace (keeping punctuation as tokens)
    - uses a provided vocab (token -> id)
    """

    def __init__(self, vocab: Dict[str, int]):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text: str) -> List[int]:
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]

        # Keep it strict like the early book version: unknown token => KeyError
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids: List[int]) -> str:
        text = " ".join(self.int_to_str[i] for i in ids)
        # remove spaces before punctuation
        text = re.sub(r"\s+([,.?\"!()\'])", r"\1", text)
        return text
