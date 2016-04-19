import csv

from collections import Iterable


class WienWahlReader(Iterable):
    def __iter__(self):
        for row in self.reader:
            newrow = {}
            for key, value in row.items():
                if key.strip() is not "":
                    newrow[key.strip()] = value
            yield newrow

    def collect(self, list=None):
        if list is None:
            list = []
        for item in self:
            list.append(item)
        return list

    def headers(self):
        return self.reader.fieldnames

    def __init__(self, file):
        if file is None or not hasattr(file, 'read'):
            raise Exception("invalid file")
        self.file = file

        self.dialect = csv.Sniffer().sniff(self.file.read(4096))
        self.file.seek(0)
        self.reader = csv.DictReader(self.file, dialect=self.dialect)


class WienWahlWriter():
    def __init__(self, file, header):
        if file is None or not hasattr(file, 'write'):
            raise Exception("invalid file")
        self.file = file
        self.dictwriter = csv.DictWriter(self.file, delimiter=";", fieldnames=header)
        self.dictwriter.writeheader()

    def write(self, row):
        self.dictwriter.writerow(row)

    def writeAll(self, rows):
        for row in rows:
            self.write(row)
