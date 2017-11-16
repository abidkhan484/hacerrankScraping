# Accepted
# Python 3

n = int(input().strip())
arr = [[int(x) for x in input().split()] for _ in range(n)]

patrol = 0; pos=0
for i in range(n):
    patrol += (arr[i][0]-arr[i][1])
    if patrol < 0:
        pos = i+1
        patrol = 0

print(pos)

