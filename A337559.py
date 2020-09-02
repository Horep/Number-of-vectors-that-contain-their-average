import itertools


def H(v):
    summand = v[1]*v[2] + v[0]*v[2] + v[0]*v[1]
    product = 3*v[0]*v[1]*v[2]
    for x in v:
        if x*summand == product:
            print(v)
            return True
    return False


def a(n):  # Calculates exact number of vectors that contain their geo mean
    if n == 1:
        prob = 1
    else:  # Brute force method
        prob = n
        for i in itertools.combinations(range(1, n+1), 3):
            x = list(i)
            Add = H(x)
            if Add is True:
                prob += 6
    return prob


def GiveSequence(n, m):  # Gives the terms a(n) between n and m (inclusive)
    x = []
    for k in range(n, m+1):
        if k == 1:
            x.append(1)
        else:
            x.append(a(k))
        print(x)
    return x
