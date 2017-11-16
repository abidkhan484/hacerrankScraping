# Accepted
# Python 3

def array_left_rotation(a, n, k):
    a2 = []
    for i in range(k, n):
        a2.append(a[i])

    for i in range(k):
        a2.append(a[i])
        
    return a2


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

