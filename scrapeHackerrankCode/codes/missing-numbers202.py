# Wrong Answer
# Python 3

n = int(input().strip())
ar = [int(x) for x in input().split()]
m = int(input().strip())
arr = list(map(int, input().split()))

ar.sort(); arr.sort()
i = 0; j = 0; pr = []
while i < n:
    if ar[i]==arr[j]:
        i += 1
        j += 1
    else:
        pr.append(arr[j])
        j += 1

print(*pr)

