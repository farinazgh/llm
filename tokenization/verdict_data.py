from __future__ import annotations

import os
import urllib.request

DEFAULT_VERDICT_URL = (
    "https://raw.githubusercontent.com/rasbt/"
    "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
    "the-the-verdict.txt"
)


def download_verdict_txt(
    file_path: str = "the-the-verdict.txt",
    url: str = DEFAULT_VERDICT_URL,
    overwrite: bool = False,
) -> str:
    """
    Downloads the verdict text file if it doesn't exist (or if overwrite=True).
    Returns the local file path.
    """
    if overwrite or not os.path.exists(file_path):
        urllib.request.urlretrieve(url, file_path)
    return file_path


def load_text(file_path: str, encoding: str = "utf-8") -> str:
    with open(file_path, "r", encoding=encoding) as f:
        return f.read()
