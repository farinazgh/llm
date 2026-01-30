from __future__ import annotations

from typing import Dict, Iterable, List


def build_vocab(tokens: Iterable[str]) -> Dict[str, int]:
    """
    Build a vocab mapping token -> integer id.
    Sorting makes it deterministic across runs.
    """
    all_words: List[str] = sorted(set(tokens))
    return {token: idx for idx, token in enumerate(all_words)}


def print_vocab_preview(vocab: Dict[str, int], limit: int = 50) -> None:
    """
    Print first `limit` vocab items for quick inspection.
    """
    for i, item in enumerate(vocab.items()):
        print(item)
        if i >= limit:
            break
