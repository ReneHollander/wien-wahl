from data.reader import Reader

with open("test.csv") as file:
    reader = Reader(file)
    for row in reader:
        print(row)
