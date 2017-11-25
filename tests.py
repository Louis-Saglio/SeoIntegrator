import unittest

import tags_processors
import utils


class MyTestCase(unittest.TestCase):

    def test_a(self):
        self.assertEqual(
            tags_processors.a("texte du lien http://lelien.com"),
            "<a href='http://lelien.com'>texte du lien</a>"
        )

    def test_format_tags(self):
        self.assertEqual(
            utils._format_tags("lorem (ipsum dolor sit( amet", '(', lambda x: f"#{x}@"),
            "lorem #ipsum dolor sit@ amet"
        )

    def test_process(self):
        info = {
            "text": 'Lorem ipsum "dolor sit" amet, consectetur "adipiscing (elit, sed https://jestocke.com( do"',
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
        self.assertEqual(
            utils.process(info),
            "Lorem ipsum <strong>dolor sit</strong> amet, consectetur <strong>adipiscing <a "
            "href='https://jestocke.com'>elit, sed</a> do</strong>"
        )


if __name__ == '__main__':
    unittest.main()
