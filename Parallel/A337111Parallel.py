import itertools
import multiprocessing as mp
import numpy as np
import time
  # EXPERIMENTAL, VERY COMPUTATIONALLY INTENSIVE

def geo_pre_mean(iterable):
    a = np.array(iterable)
    return a.prod()


def geo_avg_in_set(x):  # Checks if the pre mean is in the list
    N = len(x)
    x_1 = [y**N for y in x]
    if x_1.count(geo_pre_mean(x)) > 0:
        return True
    else:
        return False


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
        if __name__ == '__main__':
            pool = mp.Pool(mp.cpu_count())
            prob = sum(pool.map(geo_avg_in_set,
                                list(itertools.product(range(1, n+1),
                                                       repeat=4))))
    print(time.time() - start)
    return prob


print(a(100))
