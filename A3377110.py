import itertools
import numpy as np


def geo_pre_mean(iterable):  # Returns product of members of list
    a = np.array(iterable)
    return a.prod()


def geo_avg_in_set(x):  # Checks if the pre mean is in the list
    N = len(x)
    x_1 = [y**N for y in x]
    if x_1.count(geo_pre_mean(x)) > 0:
        return True
    else:
        return False


def A000188(n):
    num_of_solutions = 0
    for x in range(1, n+1):
        if x**2 % n == 0:
            num_of_solutions += 1
    return num_of_solutions


def a(n):  # Calculates exact number of vectors that contain their geo mean
    if A000188(n) == 1:  # Tests to use recurrence relation a(n) = a(n-1) + 1
        print(f"A000188({n}) = {A000188(n)}, applying recurrence relation.")
        prob = 1
        for i in itertools.product(range(1, n), repeat=3):
            x = list(i)
            Add = geo_avg_in_set(x)
            if Add is True:
                prob += 1
    else:  # Brute force method
        prob = 0
        for i in itertools.product(range(1, n+1), repeat=3):
            x = list(i)
            Add = geo_avg_in_set(x)
            if Add is True:
                prob += 1
    return prob


def GiveSequence(n, m):  # Gives the terms a(n) between n and m (inclusive)
    x = []
    for k in range(n, m+1):
        x.append(a(k))
        print(x)
    return x
