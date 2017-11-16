# Terminated due to timeout
# Python 3

n = int(input().strip())
arr = [int(p) for p in input().split()]

minim = 10**16+1
for i in range(n-1):
    pr = arr[i]; j = i+1

    while j < n:
        if pr > arr[j]:
            ia = pr-arr[j]
            if minim > ia:
                minim = ia
        j += 1
    
print(minim)

