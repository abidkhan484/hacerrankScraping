# Wrong Answer
# Python 3

n = int(input().strip())
ar = [0] * (10**4 + 1)
for i in map(int, input().split()):
    ar[i] += 1

m = int(input().strip())
arr = [0] * (10**4 + 1)
for i in map(int, input().split()):
    arr[i] += 1

i = 0; j = 0; pr = []
while j < (10**4):
    if ar[i] < arr[j]:
        print(j, end=' ')
        j += 1
        continue

    i += 1
    j += 1

'''ar.sort(); arr.sort()
i = 0; j = 0; pr = []
while i < n:
    if ar[i]==arr[j]:
        i += 1
        j += 1
    else:
        pr.append(arr[j])
        j += 1

dList = []
for i in range(len(pr)-1):
    if pr[i]==pr[i+1]:
        dList.append(i+1)

for i in dList:
    del pr[i]

print(*pr)
'''

