import csv

from collections import Iterable


class Reader(Iterable):
    def __iter__(self):
        dialect = csv.Sniffer().sniff(self.file.read(1024))
        self.file.seek(0)
        reader = csv.DictReader(self.file, dialect=dialect)
        for row in reader:
            yield row

    def collect(self, list=None):
        if list is None:
            list = []
        for item in self:
            list.append(item)
        return list

    def __init__(self, file):
        self.file = file
