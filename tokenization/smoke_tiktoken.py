from __future__ import annotations

from pathlib import Path

from tokenization.tiktoken_gpt2 import (
    print_tiktoken_version,
    get_gpt2_tokenizer_gpt2_encoding,
    encode_with_endoftext,
    encode,
    gpt2_decode,
)


def main() -> None:
    print_tiktoken_version()

    gpt2_tokenizer = get_gpt2_tokenizer_gpt2_encoding()

    text = (
        "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
        "of someunknownPlace."
    )
    integers = encode_with_endoftext(gpt2_tokenizer, text)
    print("simple text gpt2 encoding")
    print(integers)

    strings = gpt2_decode(gpt2_tokenizer, integers)
    print("simple text gpt2 decoding")
    print(strings)

    # Adjust path to where your file actually is:
    # You currently have tokenization/the-verdict.txt
    verdict_path = Path("C:\\polaris\\code\\PythonProject\\llm\\tokenization\\the-verdict.txt")

    raw_text = verdict_path.read_text(encoding="utf-8")
    enc_text = encode(gpt2_tokenizer, raw_text)
    print("length of encoded text:")
    print(len(enc_text))

    # The book shows shifting input->target pairs
    enc_sample = enc_text  # fix: your snippet used enc_sample but never defined it

    context_size = 4
    x = enc_sample[:context_size]
    y = enc_sample[1: context_size + 1]
    print(f"x: {x}")
    print(f"y:      {y}")

    for i in range(1, context_size + 1):
        context = enc_sample[:i]
        desired = enc_sample[i]
        print(context, "---->", desired)

    for i in range(1, context_size + 1):
        context = enc_sample[:i]
        desired = enc_sample[i]
        print(gpt2_decode(gpt2_tokenizer, context), "---->", gpt2_decode(gpt2_tokenizer, [desired]))


if __name__ == "__main__":
    main()
