# Accepted
# Python 3

n = int(input().strip())

for _ in range(n):
    st = input().strip()

    l = len(st)
    c = 0
    for i in range(l//2):
        if st[i] != st[l-i-1]:
            tmp = ord(st[i])
            temp = ord(st[l-i-1])
            tmp = abs(tmp-temp)
            c += tmp

    print(c)

