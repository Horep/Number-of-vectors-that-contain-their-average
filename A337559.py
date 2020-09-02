def b(n):
    prob = 0
    for a in range(1, n+1):
        if 2*a*n % (a+n) == 0 and a != n:
            print(f"{a},{2*a*n//(a+n)},{n}")
            prob += 6
    return prob


def first(n):
    lst = [1]
    for i in range(2, n+1):
        lst.append(1 + lst[i-2] + b(i))
    return lst
