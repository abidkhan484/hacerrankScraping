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

# i can use set here
dList = []
for i in range(len(pr)-1):
    if pr[i]==pr[i+1]:
        dList.append(i+1)

for i in dList:
    del pr[i]

# this loop check if the list has value >100 or not?
li = []
for i in range(len(pr)):
    if pr[i] > (pr[0] + 100):
        break
    li.append(pr[i])

print(*li)

