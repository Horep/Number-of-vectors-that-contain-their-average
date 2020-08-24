import random
import itertools
from GeometricMean import geo_pre_mean


def build_set(N, k):  # Build set S from 1 to k with N elements
    x = []
    for i in range(N):
        x.append(random.randint(1, k))
    x.sort()
    return x


def avg_in_set(x):
    N = len(x)
    x_1 = [N*y for y in x]
    if x_1.count(sum(x)) > 0:
        return True
    else:
        return False


def A_est(N, k):  # Estimates probability from 'iterations' number of trials
    prob = 0
    iterations = k**N / 8
    for i in range(iterations):
        x = build_set(N, k)
        Add = avg_in_set(x)
        if Add is True:
            prob += 1
    return prob/iterations * k**N


def G_est(N, k):  # Estimates probability from 'iterations' number of trials
    prob = 0
    iterations = k**N / 8
    for i in range(iterations):
        x = build_set(N, k)
        Add = geo_avg_in_set(x)
        if Add is True:
            prob += 1
    return prob/iterations * k**N


def A(N, k):  # Calculates exact number of sequences
    prob = 0
    for i in itertools.product(range(0, k+1), repeat=N):
        Add = avg_in_set(list(i))
        if Add is True:
            print(list(i))
            prob += 1

    return prob


def geo_avg_in_set(x):
    N = len(x)
    x_1 = [y**N for y in x]
    if x_1.count(geo_pre_mean(x)) > 0:
        return True
    else:
        return False


def G(N, k):  # Calculates exact number
    prob = 0
    for i in itertools.product(range(1, k+1), repeat=N):
        x = list(i)
        Add = geo_avg_in_set(x)
        if Add is True:
            prob += 1
    return prob


def GiveList(y, N, num):  # Returns a list from k=1 to k=num for function y
    x = []
    for k in range(1, num+1):
        x.append(y(N, k))
        print(x)
    return x


def GiveTable(y, N_num, k_num):  # Returns a list of GiveList lists for N
    x = []
    for N in range(1, N_num+1):
        x.append(GiveList(y, N, k_num))
        print(x)
    return x


def give_nontrivial_consecutive(y, N, num):  # Calculates non-trivial 1st diff
    x = [0]
    for k in range(2, num+1):
        x.append(y(N, k)-y(N, k-1)-1)
        print(x)
    return x


def give_G_successive_nontrivial_four_ratio(N):
    return G(N, 4) - 4, G(N+1, 4) - 4
