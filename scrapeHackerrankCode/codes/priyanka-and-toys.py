# Accepted
# Python 3

n = int(input().strip())
arr = [int(x) for x in input().split()]

total = 1; arr.sort()

p = 0
for i in range(n):
    if (arr[p]+4) < arr[i]:
        total += 1; p = i

print(total)

