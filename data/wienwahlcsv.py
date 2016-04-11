import csv

from collections import Iterable


class WienWahlReader(Iterable):
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
        if file is None or not hasattr(file, 'read'):
            raise Exception("invalid file")
        self.file = file


class WienWahlWriter():
    def __init__(self, file):
        if file is None or not hasattr(file, 'write'):
            raise Exception("invalid file")
        self.file = file
        self.dictwriter = None

    def write(self, row):
        if not self.dictwriter:
            fieldnames = list(row.keys())
            self.dictwriter = csv.DictWriter(self.file, delimiter=";", fieldnames=fieldnames)
            self.dictwriter.writerow(dict((fn, fn) for fn in fieldnames))

        self.dictwriter.writerow(row)

    def writeAll(self, rows):
        for row in rows:
            self.write(row)
