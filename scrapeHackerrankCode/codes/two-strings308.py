# Accepted
# Python 3

q = int(input().strip())
for a0 in range(q):
    s1 = set(input().strip())
    s2 = set(input().strip())

    if s1.intersection(s2):
        print('YES')
    else:
        print('NO')
    

