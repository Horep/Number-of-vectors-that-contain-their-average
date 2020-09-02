import itertools


def num_of_perms(v):
    mysetlen = len(set(v))
    if mysetlen == 4:
        return 24
    elif mysetlen == 3:
        return 12
    elif mysetlen == 2:
        return 6
    elif mysetlen == 1:
        return 1


def H(v):
    summand = v[1]*v[2]*v[3] + v[0]*v[2]*v[3] + v[0]*v[1]*v[3] + v[0]*v[1]*v[2]
    product = 4*v[0]*v[1]*v[2]*v[3]
    for x in v:
        if x*summand == product:
            return True
    return False


def a(n):  # Calculates exact number of vectors that contain their geo mean
    if n == 1:
        prob = 1
    else:  # Brute force method
        prob = 0
        for i in itertools.combinations_with_replacement(range(1, n+1), 4):
            x = list(i)
            Add = H(x)
            if Add is True:
                prob += num_of_perms(x)
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
