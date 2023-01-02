using Pkg
Pkg.add("DataStructures")
using DataStructures

function give_incremental(n::Int64)
    if n==1 || minimum([(i^2 % n) for i ∈ 1:(n-1)]) > 0  # if x^2 == 0 (mod n) has more than one solution this set has a minimum of 0.
        return 1
    end
    count = 1  # takes care of (n,n,n)
    for b ∈  1:n, a ∈ 1:(b-1)  # a and b must be different
        if b*n == a^2 || a*n == b^2  # checking if a*b*n = a^3 or b^3
            count = count + 6
        end
    end
    return count
end


function first(n::Int64)
    total = 0
    for i in 1:n
        total = total + give_incremental(i)
        print(total,"\n")
    end
end
