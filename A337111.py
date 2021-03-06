import itertools
import time
from GeometricMean import geo_avg_in_set


def A000189(n):
    num_of_solutions = 0
    for x in range(1, n+1):
        if x**3 % n == 0:
            num_of_solutions += 1
    return num_of_solutions


def a(n):  # Calculates exact number of vectors that contain their geo mean
    start = time.time()
    if n == 1:
        return 1
    elif A000189(n) == 1:  # Tests to use recurrence relation a(n) = a(n-1) + 1
        print(f"A000189({n}) = 1, applying recurrence relation.")
        prob = a(n-1) + 1
    else:  # Brute force method
        prob = 0
        for i in itertools.product(range(1, n+1), repeat=4):
            x = list(i)
            Add = geo_avg_in_set(x)
            if Add is True:
                prob += 1
    print(time.time() - start)
    return prob


def GiveSequence(n, m):  # Gives the terms a(n) between n and m (inclusive)
    x = []
    for k in range(n, m+1):
        if k == 1:
            x.append(1)
        elif len(x) > 0:
            if A000189(k) == 1:
                print(f"A000189({k}) = 1, applying recurrence relation.")
                x.append(x[len(x)-1] + 1)
            else:
                x.append(a(k))
        else:
            x.append(a(k))
        print(x)
    return x
