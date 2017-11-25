from typing import List, Tuple

import data_IO
import tags_processors
import utils


def format_text() -> List[Tuple[str, str]]:
    rep = []
    data = data_IO.read_input()
    info = {
        "text": "",
        "tags": (
            {
                "char": "\"",
                "function": tags_processors.strong
            },
            {
                "char": "(",
                "function": tags_processors.a
            }
        )
    }
    for row in data:
        info["text"] = row[1]
        rep.append((row[0], utils.process(info)))
    return rep


if __name__ == '__main__':
    print(data_IO.out(format_text()))
