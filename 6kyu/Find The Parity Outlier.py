def find_outlier(integers):
    evens = []
    odds = []
    for i in integers:
        if i % 2 > 0:
            odds.append(i)
        if i % 2 == 0:
            evens.append(i)
    if len(evens) > len(odds):
        return odds[0]
    else:
        return evens[0]