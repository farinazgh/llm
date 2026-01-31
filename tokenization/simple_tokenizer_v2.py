from __future__ import annotations

import re
from typing import Dict, List


class SimpleTokenizerV2:
    """
    Version 2:
    - splits on a slightly richer punctuation set (, . : ; ...)
    - replaces unknown tokens with <|unk|> instead of crashing
    """

    def __init__(self, vocab: Dict[str, int], unk_token: str = "<|unk|>"):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}
        self.unk_token = unk_token

        if self.unk_token not in self.str_to_int:
            raise ValueError(f"unk_token {self.unk_token!r} is not in vocab.")

    def encode(self, text: str) -> List[int]:
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]

        preprocessed = [
            item if item in self.str_to_int else self.unk_token
            for item in preprocessed
        ]

        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids: List[int]) -> str:
        text = " ".join(self.int_to_str[i] for i in ids)
        text = re.sub(r"\s+([,.:;?\"!()\'])", r"\1", text)
        return text
