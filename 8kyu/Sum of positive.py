def positive_sum(arr):
    a = []
    for i in arr:
        if i > 0:
            a.append(i)
    return sum(a)