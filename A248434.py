import itertools


def avg_in_set(x):
    N = len(x)
    x_1 = [N*y for y in x]
    if x_1.count(sum(x)) > 0:
        return True
    else:
        return False


def a(n):  # Calculates exact number of sequences
    prob = 0
    for i in itertools.product(range(0, n+1), repeat=3):
        Add = avg_in_set(list(i))
        if Add is True:
            prob += 1

    return prob
