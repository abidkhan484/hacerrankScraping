# Wrong Answer
# Python 3

# simple combinatorics function
def make_combination(n, r):
    total = 1
    for i in range(n, r, -1):
        total *= i

    another = 1;     
    for i in range(1, n-r+1):
        another *= i

    return total//another

per, n = map(int, input().split())
m = per/100
f = 1-m

# here n is given
# and k=2 according to the condition
# binomial distribution: nCr*(m**r)*(f**(n-r))
total=0; k=2
for i in range(k):
    # total is the adding the distribution bcoz
    # the problem says the word 'at least'
    total += (make_combination(n, i)*(m**i)*(f**(n-i)))

print(round(total, 3))

total=0
for i in range(k, n+1):
    # total is the adding the distribution bcoz
    # the problem says the word 'at least'
    total += (make_combination(n, i)*(m**i)*(f**(n-i)))

print(round(total, 3))

