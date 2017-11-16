# Accepted
# Python 2

# simple combinatorics function
def make_combination(n, k):
    total = 1
    for i in range(n, k, -1):
        total *= i

    another = 1;     
    for i in range(1, n-k+1):
        another *= i

    return total//another

male, female = 1.09, 1
m = male/(male+female)
f = female/(male+female)

# here n=6 bcoz the problem says 6 children
# and k=3 coz at least 3 are boys out of 6 children
# binomial distribution: nCr*(m**r)*(f**(n-r))
n=6; k=3; total=0
for i in range(k, n+1):
    # total is the adding the distribution bcoz
    # the problem says the word 'at least'
    total += (make_combination(n, i)*(m**i)*(f**(n-i)))

print round(total, 3)

