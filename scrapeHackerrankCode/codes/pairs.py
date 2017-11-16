# Accepted
# Python 3

# this problem is still unsolved

n, k = map(int, input().split())
arr = [int(p) for p in input().split()]

arr.sort(); j=1; count=0
for i in range(n):

    if arr[i] + k > arr[-1]:
        break

    while (j < n):
        if arr[j] > arr[i]+k:
            break
        if arr[j]==arr[i]+k:
            count += 1
        j += 1

    j -= 1
    
print(count)

