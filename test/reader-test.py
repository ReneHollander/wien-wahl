import unittest

import sys, os

sys.path.insert(0, os.path.abspath(__file__ + "/.."))

from data.reader import Reader


class ReaderTest(unittest.TestCase):
    def test_valid_file(self):
        with open("valid.csv") as file:
            reader = Reader(file)
            list = reader.collect()
            self.assertEqual(list, [
                {'Column1': '1', 'Column3': 'World', 'Column2': 'Hello'},
                {'Column1': '2', 'Column3': 'Welt', 'Column2': 'Hallo'},
                {'Column1': '3', 'Column3': 'monde', 'Column2': 'Bonjour'}
            ])

    def test_invalid_file(self):
        with open("invalid.csv") as file:
            reader = Reader(file)
            self.assertRaises(Exception, reader.collect)

    def test_umlauts(self):
        with open("umlauts.csv") as file:
            reader = Reader(file)
            list = reader.collect()
            self.assertEqual(list, [
                {'Column1': 'ä', 'Column2': 'ü'},
                {'Column1': 'ü', 'Column2': 'ä'}
            ])

    def test_invalid_fileobject(self):
        self.assertRaises(Exception, Reader, None)

    def test_iterator(self):
        with open("valid.csv") as file:
            reader = Reader(file)
            trueresults = [
                {'Column1': '1', 'Column3': 'World', 'Column2': 'Hello'},
                {'Column1': '2', 'Column3': 'Welt', 'Column2': 'Hallo'},
                {'Column1': '3', 'Column3': 'monde', 'Column2': 'Bonjour'}
            ]
            for row in reader:
                if row in trueresults:
                    self.assertEqual(True, True)
                else:
                    self.assertEqual(False, True)


if __name__ == "__main__":
    unittest.main()
