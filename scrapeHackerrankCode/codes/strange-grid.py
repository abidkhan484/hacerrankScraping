# Accepted
# Python 3

p, r = input().split()
p, r = int(p), int(r)

print((((p-1)//2)*10)+(r*2-2)) if (p&1) else print((((p-1)//2)*10)+(r*2-1))
