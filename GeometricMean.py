import numpy as np


def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod()**(1/len(a))


def geo_pre_mean(iterable):
    a = np.array(iterable)
    return a.prod()


def geo_avg_in_set(x):  # Checks if the pre mean is in the list
    N = len(x)
    if x.count(x[0]) == N - 1 or x.count(x[1]) == N - 1:
        return False
    x_1 = [y**N for y in x]
    if x_1.count(geo_pre_mean(x)) > 0:
        return True
    else:
        return False


def ari_mean(iterable):
    a = np.array(iterable)
    return a.sum()
