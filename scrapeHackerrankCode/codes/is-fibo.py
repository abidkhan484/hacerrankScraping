# Accepted
# Python 3

def fibo(n, p=1, q=1):
    if n == p:
        return 'IsFibo'
    if n < p:
        return 'IsNotFibo'
    return fibo(n, p+q, p)

for _ in range(int(input().strip())):
    print(fibo(int(input().strip())))

