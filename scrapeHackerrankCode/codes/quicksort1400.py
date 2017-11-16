# Accepted
# Python 3

def quicksort(li):
    pivot = li[0]
    l = len(li)

    right = []; left = []
    for i in range(1, l):
        if pivot < li[i]:
            right.append(li[i])
        elif pivot >= li[i]:
            left.append(li[i])
    left.append(pivot)
    left.extend(right)
    return left

n = int(input().strip())
li = [int(c) for c in input().split()]

li = quicksort(li)
for _ in li:
    print(_, end=' ')

