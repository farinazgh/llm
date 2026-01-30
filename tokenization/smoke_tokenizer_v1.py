from __future__ import annotations

import re

from tokenization.simple_tokenizer_v1 import SimpleTokenizerV1
from tokenization.vocab import build_vocab, print_vocab_preview


def basic_preprocess(text: str) -> list[str]:
    """
    Minimal preprocessing to create tokens for vocab building.
    This mirrors the tokenizer split rule.
    """
    tokens = re.split(r'([,.?_!"()\']|--|\s)', text)
    return [t.strip() for t in tokens if t.strip()]


def main() -> None:
    # In your notebook earlier you likely had: preprocessed = [...]
    # Here we create it in a self-contained way so PyCharm can run it.
    sample_corpus = (
        "It's the last he painted, you know, "
        'Mrs. Gisburn said with pardonable pride.'
    )

    preprocessed = basic_preprocess(sample_corpus)

    vocab = build_vocab(preprocessed)
    vocab_size = len(vocab)

    print("vocab_size:", vocab_size)
    print("vocab preview:")
    print_vocab_preview(vocab, limit=50)

    tokenizer = SimpleTokenizerV1(vocab)

    text = (
        "It's the last he painted, you know, "
        "Mrs. Gisburn said with pardonable pride."
    )

    ids = tokenizer.encode(text)
    print("encoded ids:", ids)

    decoded = tokenizer.decode(ids)
    print("decoded:", decoded)


if __name__ == "__main__":
    main()
