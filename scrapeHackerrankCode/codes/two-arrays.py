# Accepted
# Python 3

def check_permute():
    n, k = map(int, input().split())
    a = [int(p) for p in input().split()]
    b = list(map(int, input().split()))

    a.sort(); b.sort(reverse=True)
    for i in range(n):
        if (a[i]+b[i]) < k:
            print('NO')
            break
    else:
        print('YES')

for _ in range(int(input().strip())):
    check_permute()

