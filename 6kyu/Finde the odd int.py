import collections

def find_it(seq):
    a = collections.Counter(seq)
    for i in a:
        if a[i] % 2 == 1:
            return i