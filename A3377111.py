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


def a(n):  # Calculates exact number of vectors that contain their geo mean
    prob = 0
    for i in itertools.product(range(1, n+1), repeat=4):
        x = list(i)
        Add = geo_avg_in_set(x)
        if Add is True:
            prob += 1
    return prob
