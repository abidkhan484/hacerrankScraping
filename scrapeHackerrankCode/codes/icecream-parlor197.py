# Wrong Answer
# Python 3

def goodForNothing():

    m = int(input().strip())
    n = int(input().strip())
    arr = [int(p) for p in input().split()]

    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i]+arr[j]==m:
                if arr[i]==min(arr[i], arr[j]):
                    print(i+1, j+1)
                    return                


for _ in range(int(input().strip())):
    goodForNothing()

