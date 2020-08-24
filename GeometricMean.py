import numpy as np


def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod()**(1.0/len(a))


def geo_pre_mean(iterable):
    a = np.array(iterable)
    return a.prod()


def ari_mean(iterable):
    a = np.array(iterable)
    return a.sum()