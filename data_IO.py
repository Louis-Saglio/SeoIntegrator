import csv
from typing import List, Tuple

import settings
import text_indentation


def _read_csv() -> Tuple[str, ...]:
    with open(settings.INPUT_FILE, newline='') as f:
        return tuple(csv.reader(f, delimiter=';'))


def _clean_data(data: Tuple[str, ...]) -> Tuple[Tuple[str, str], ...]:
    return tuple((row[0].split()[0], row[1].replace(')', '(')) for row in data if row not in (['', ''], ['']))


def read_input() -> Tuple[Tuple[str, str], ...]:
    return _clean_data(_read_csv())


def out(data: List[Tuple[str, str]]) -> str:
    return text_indentation.format_rows(data)
