from __future__ import annotations

from typing import Dict, Iterable, List, Sequence


DEFAULT_SPECIAL_TOKENS: Sequence[str] = ("<|endoftext|>", "<|unk|>")


def build_vocab(tokens: Iterable[str], special_tokens: Sequence[str] = DEFAULT_SPECIAL_TOKENS) -> Dict[str, int]:
    """
    Build vocab mapping token -> id.
    - Deterministic ordering via sorting.
    - Appends special tokens at the end (like the book example).
    """
    all_tokens: List[str] = sorted(set(tokens))
    for st in special_tokens:
        if st not in all_tokens:
            all_tokens.append(st)
    return {token: idx for idx, token in enumerate(all_tokens)}


def print_vocab_tail(vocab: Dict[str, int], n: int = 5) -> None:
    """
    Print last n vocab items.
    """
    items = list(vocab.items())[-n:]
    for item in items:
        print(item)
