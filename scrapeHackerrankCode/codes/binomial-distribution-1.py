# Accepted
# Python 2

# simple combinatorics function
def make_combination(n, r):
    total = 1
    for i in range(n, r, -1):
        total *= i

    another = 1;     
    for i in range(1, n-r+1):
        another *= i

    return total//another

# hits the target 4 times out of 5
m = .8
f = .2
n = 4 # fires 4 shots (see the condition)

# binomial distribution: nCr*(m**r)*(f**(n-r))
total=0; k=3
for i in range(k, n+1):
    # total is the adding the distribution bcoz
    # the problem says the word 'at least'
    total += (make_combination(n, i)*(m**i)*(f**(n-i)))

print round(total, 3)

total=0; k=n-k+1
for i in range(k):
    # total is the adding the distribution bcoz
    # the problem says the word 'at least'
    total += (make_combination(n, i)*(m**i)*(f**(n-i)))

print round(total, 3)

