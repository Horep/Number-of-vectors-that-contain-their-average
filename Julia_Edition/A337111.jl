function give_incremental(n::Int64)
    if n==1 || minimum([(i^3 % n) for i ∈ 1:(n-1)]) > 0  # if x^3 == 0 (mod n) has more than one solution this set has a minimum of 0.
        return 1
    end
    count = 1  # takes care of (n,n,n,n)
    for c ∈  1:n, b ∈ 1:c, a ∈ 1:b  # (a,b,c,n) subject to a≤b≤c≤n
        val = a*b*c*n
        if val ∈ [a^4, b^4, c^4] && val !== n^4  # checking if a*b*c*n = a^4, b^4, c^4 but not n^4
            count = count + give_permutations(a, b, c, n)
        end
    end
    return count
end

function give_permutations(a, b, c, n)
    if a == b || b == c || c == n
        return 12  # of the form (a,a,c,n), only 12 permutations
    else
        return 24  # of the form (a,b,c,n), 24 permutations
    end
end

function first(n::Int64)
    total = 0
    for i in 1:n
        total = total + give_incremental(i)
        print(total,"\n")
    end
end