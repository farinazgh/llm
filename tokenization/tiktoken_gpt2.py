from __future__ import annotations

from importlib.metadata import version
import tiktoken


def print_tiktoken_version() -> None:
    print("tiktoken version:", version("tiktoken"))


def get_gpt2_tokenizer_gpt2_encoding():
    return tiktoken.get_encoding("gpt2")


def encode_with_endoftext(tokenizer, text: str) -> list[int]:
    # Allow the special token <|endoftext|> in the input
    return tokenizer.encode(text, allowed_special={"<|endoftext|>"})


def encode(tokenizer, text: str) -> list[int]:
    return tokenizer.encode(text)


def gpt2_decode(tokenizer, ids: list[int]) -> str:
    return tokenizer.decode(ids)
