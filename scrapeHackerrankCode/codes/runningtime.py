# Accepted
# Python 3

def insertion_sort(l):
    c = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            c += 1
            j -= 1
        l[j+1] = key
    return c
 
m = int(input().strip())
ar = [int(i) for i in input().strip().split()]

print(insertion_sort(ar))
