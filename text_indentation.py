from typing import Tuple, Iterable


def indent_text(text: str, line_size: int=100, indent_level: int=2, indent_size: int=4) -> str:
    rep = str()
    line_size = line_size - 2 - indent_size * indent_level
    for i in range(0, len(text), line_size):
        rep += f'{" " * indent_level * indent_size}"{text[i:line_size+i]}"\n'
    return rep


def format_row(row: Tuple[str, str], line_size: int=100, indent_level: int=2, indent_size: int=4) -> str:
    city, text, indent = *row, (' ' * indent_size * (indent_level-1))
    return f'{indent}"{city}": _(\n{indent_text(text, line_size, indent_level, indent_size)}{indent}),\n'


def format_rows(rows: Iterable[Tuple[str, str]], line_size: int=100, indent_level: int=2, indent_size: int=4) -> str:
    rep = str('{\n')
    for row in rows:
        rep += format_row(row, line_size, indent_level, indent_size)
    return rep + '\n}'
