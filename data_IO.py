import csv
from typing import List, Tuple

import settings
import text_indentation


def _read_csv() -> Tuple[str, ...]:
    with open(settings.INPUT_FILE, newline='') as f:
        return tuple(csv.reader(f, delimiter=';'))


def _clean_data(data: Tuple[str, ...]) -> Tuple[Tuple[str, str], ...]:
    rep = []
    for row in data:
        if row not in (['', ''], ['']):
            try:
                # Décomenter la ligne suivante pour trouver plus facilement les erreurs de formatage dans le texte.
                # print(row[0])
                rep.append((row[0].split()[0], row[1].replace(')', '(')))
            except IndexError:
                print(row)
                exit(1)
    return tuple(rep)


def read_input() -> Tuple[Tuple[str, str], ...]:
    return _clean_data(_read_csv())


def out(data: List[Tuple[str, str]]) -> str:
    return text_indentation.format_rows(data)
