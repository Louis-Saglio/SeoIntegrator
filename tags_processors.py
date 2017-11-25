def strong(word: str) -> str:
    return f"<strong>{word}</strong>"


def a(word: str) -> str:
    word = word.split()
    text = ' '.join(word[:-1])
    href = word[-1]
    return f"<a href='{href}'>{text}</a>"
