from __future__ import annotations

import re

from tokenization.simple_tokenizer_v2 import SimpleTokenizerV2
from tokenization.vocab2 import build_vocab, print_vocab_tail


def basic_preprocess(text: str) -> list[str]:
    tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    return [t.strip() for t in tokens if t.strip()]


def main() -> None:
    corpus = (
        "\"It's the last he painted, you know,\" "
        "Mrs. Gisburn said with pardonable pride."
    )

    preprocessed = basic_preprocess(corpus)

    vocab = build_vocab(preprocessed, special_tokens=("<|endoftext|>", "<|unk|>"))
    print("vocab_size:", len(vocab))
    print("vocab tail:")
    print_vocab_tail(vocab, n=5)

    tokenizer = SimpleTokenizerV2(vocab)

    # Add a word that's not in vocab to prove <|unk|> works
    text = corpus + " UNSEENWORD"
    ids = tokenizer.encode(text)
    print("ids:", ids)

    decoded = tokenizer.decode(ids)
    print("decoded:", decoded)


if __name__ == "__main__":
    main()
