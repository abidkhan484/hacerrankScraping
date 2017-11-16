# Accepted
# Python 3

def is_triangle(a, b, c):
    if ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
        return True
    return False

n = int(input().strip())
sticks = [int(x) for x in input().split()]

sticks.sort()
for i in range(n-1, 1, -1):
    if is_triangle(sticks[i], sticks[i-1], sticks[i-2]):
        print(sticks[i-2], sticks[i-1], sticks[i])
        break
else:
    print(-1)

