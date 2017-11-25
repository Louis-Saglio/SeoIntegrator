from typing import Callable


def _format_tags(text: str, char: str, func: Callable[[str], str]) -> str:
    text = text.split(char)
    return ''.join([func(word) if word in text[1::2] else word for word in text])


def process(data_: dict) -> str:
    text = data_["text"]
    for balise in data_["tags"]:
        text = _format_tags(text, balise["char"], balise["function"])
    return text
