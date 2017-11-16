# Accepted
# Python 3

m, n = input().split()
m, n = int(m), int(n)

x, y = m//2, n//2
if not (m&1) and not(n&1):
    print(x*y)

elif (m&1) and (n&1):
    print((x*y)+x+y+1)

else:
    print((x*y)+y) if m&1 else print((x*y)+x)

