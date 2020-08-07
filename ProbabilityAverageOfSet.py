import random
import itertools


def build_set(N, k):  # Build set S from 1 to k with N elements
    x = []
    for i in range(N):
        x.append(random.randint(1, k))
    x.sort()
    return x


def avg_in_set(x):
    avg = sum(x)/len(x)
    if x.count(avg) > 0:
        return True
    else:
        return False


def P_est(N, k):
    prob = 0
    iterations = 10000
    for i in range(iterations):
        x = build_set(N, k)
        Add = avg_in_set(x)
        if Add is True:
            prob += 1
    t = k**N
    print(f"Lower Bound {k}**(1-{N}) = {k**(1-N)}")
    print(f"Number of true cases = {prob}")
    print(f"Number of elements = {t}")
    return prob/t


def P(N, k):
    prob = 0
    for i in itertools.product(range(1, k+1), repeat=N):
        Add = avg_in_set(list(i))
        if Add is True:
            prob += 1
    t = k**N
    print(f"Lower Bound {k}**(1-{N}) = {k**(1-N)}")
    print(f"Number of true cases = {prob}")
    print(f"Number of elements = {t}")
    return prob/t
