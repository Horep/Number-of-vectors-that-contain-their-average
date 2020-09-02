def num_of_perms(v):
    mysetlen = len(set(v))
    if mysetlen == 4:
        return 24
    elif mysetlen == 3:
        return 12
    elif mysetlen == 1:
        return 1


def b(n):
    prob = 0
    for b in range(1, n+1):
        for a in range(1, b+1):
            if 3*a*b*n % (a*b+a*n+b*n) == 0 and a != n:
                c = 3*a*b*n // (a*b+a*n+b*n)
                v = [a, b, c, n]
                prob += num_of_perms(v)
    return prob


def first(n):
    lst = [1]
    for i in range(2, n+1):
        lst.append(1 + lst[i-2] + b(i))
    return lst
