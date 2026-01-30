from __future__ import annotations

from tokenization.basic_tokenizer import basic_tokenize, demo_regex_splits
from tokenization.verdict_data import download_verdict_txt, load_text


def main() -> None:
    file_path = download_verdict_txt(file_path="C:\\polaris\\code\\PythonProject\\llm\\tokenization\\the-verdict.txt")
    raw_text = load_text(file_path)

    print("Total number of characters:", len(raw_text))
    print(raw_text[:99])

    # 2) tokenize a single line example
    demo_regex_splits()
    #
    # 3) Tokenize the full the-verdict.txt and print token count
    preprocessed = basic_tokenize(raw_text)
    print("Number of tokens:", len(preprocessed))


if __name__ == "__main__":
    main()
