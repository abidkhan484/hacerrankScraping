# Wrong Answer
# Python 3

m, n = input().split()
m, n = int(m), int(n)

m = m*n
n = m//4
m = m/4

print(n+1) if m>n else print(n)

