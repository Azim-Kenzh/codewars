def high_and_low(numbers):
    a = numbers.split()
    max_ = max(list(map(int, a)))
    min_ = min(list(map(int, a)))
    return f"{max_} {min_}"