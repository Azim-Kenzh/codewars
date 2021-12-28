def count_bits(n):
    a = bin(n)
    b = list(a)
    c = list(map(int, b[2:]))
    return sum(c)

"""OR"""

def count_bits(n):
    return bin(n).count("1")