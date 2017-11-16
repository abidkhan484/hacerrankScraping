# Accepted
# Python 3

#!/bin/python3

def minimumAbsoluteDifference(n, arr):

    minim = 10000000001
    arr.sort()
    for i in range(1, n):
        tmp = arr[i] - arr[i-1]
        if tmp < minim:
            minim = tmp

    return minim

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)

