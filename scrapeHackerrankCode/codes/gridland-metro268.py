# Wrong Answer
# Python 3

n, m, k = [int(x) for x in input().split()]

# now n is total train track
n *= m

for _ in range(k):
    p, q, r = [int(x) for x in input().split()]
    
    r = r-q+1
    n -= r

print(n)

