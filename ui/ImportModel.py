"""
Autor: Rene Hollander 5BHIT
"""

from data.reader import Reader


class ImportModel():
    def __init__(self):
        self.items = []

    def read(self, path):
        with open(path) as file:
            reader = Reader(file)
            self.items.clear()
            reader.collect(self.items)
