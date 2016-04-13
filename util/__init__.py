def read_fully(filename):
    with open(filename) as file:
        return file.read()


def first(the_iterable, condition=lambda x: True):
    for i in the_iterable:
        if condition(i):
            return i
