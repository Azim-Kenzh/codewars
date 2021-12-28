import collections

def find_it(seq):
    a = collections.Counter(seq)
    for i in a:
        if a[i] % 2 == 1:
            return i


"""OR"""


def find_it(seq):
    for i in seq:
        if  seq.count(i) % 2 != 0:
            return i
