# Accepted
# Python 3

p, r = input().split()
p, r = int(p), int(r)

if not (p&1):
    print((((p-1)//2)*10)+(r*2-1))
else:
    print((((p-1)//2)*10)+(r*2-2))

