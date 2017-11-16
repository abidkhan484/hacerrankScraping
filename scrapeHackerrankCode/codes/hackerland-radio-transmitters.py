# Accepted
# Python 3

n, k = map(int, input().split())
mylist = list(map(int, input().split()))

mylist.sort()

p = 0; count = 1; tmp = 1
for i in range(1, n):

    if mylist[i] > (mylist[p]+k):
        if (i-p) == 1:
            count += 1; p = i
        else:
            if tmp:
                if (mylist[i-1]+k) >= mylist[i]:
                    tmp = 0; p = i-1
                else:
                    count += 1; p = i
            else:
                count += 1; p = i; tmp = 1

print(count)

