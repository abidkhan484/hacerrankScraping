# Terminated due to timeout
# Python 3

#!/bin/python3

def minimumAbsoluteDifference(n, arr):

    minim = 100000001
    for i in range(n-1):
        j = i+1
        while j < n:
            diff = arr[i] - arr[j]
            if not diff:
                return diff
            if diff < 0:
                diff = abs(diff)
            if minim > diff:
                minim = diff
            j += 1

    return minim

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)

