# Accepted
# Python 3

student, sub = map(int, input().split())

arr = [[float(p) for p in input().split()] for _ in range(sub)]

for i in list(zip(*arr)):
    print('%.1f' %(sum(i)/sub))

