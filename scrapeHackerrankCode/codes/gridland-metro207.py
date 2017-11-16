# Wrong Answer
# Python 3

n, m, k = map(int, input().split())

total = n*m

for i in range(k):
    p, q, r = map(int, input().split())
    total -= (r-q+1)

print(total)

