# Accepted
# Python 3

def sherlockArray():
    
    n = int(input().strip())
    arr = [int(p) for p in input().split()]

    if n==1:
        print('YES')
        return
    
    leftSum = 0; rightSum = 0
    for i in range(1, n):
        rightSum += arr[i]

    for i in range(n-1):
        if leftSum > rightSum:
            print('NO')
            return
        if leftSum == rightSum:
            print('YES')
            return
        leftSum += arr[i]
        rightSum -= arr[i+1]

    print('NO')
    return

for _ in range(int(input().strip())):
    sherlockArray()

