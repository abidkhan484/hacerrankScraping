# Accepted
# Python 3

def quicksort(li):
    pivot = li[0]
    l = len(li); t=l-1

    for i in range(t, 0, -1):
        if pivot <= li[i]:
            l -= 1
            temp = li[l]
            li[l] = li[i]
            li[i] = temp

    temp = li[l-1]
    li[l-1] = li[0]
    li[0] = temp

    return li

n = int(input().strip())
li = [int(_) for _ in input().split()]


li = quicksort(li)
for _ in li:
    print(_, end=' ')

