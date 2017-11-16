# Wrong Answer
# Python 3

m, n = input().split()
m, n = int(m), int(n)

if m==1 or n==1:
    m = m*n
    n = m//2
    m = m/2

    print(n+1) if m>n else print(n)
else:
    m = m*n
    n = m//4
    m = m/4

    print(n+1) if m>n else print(n)

