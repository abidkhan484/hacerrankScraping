# Wrong Answer
# Python 3

n, k = [int(x) for x in input().split()]
mylist = [int(x) for x in input().split()]

mylist.sort()

p = 0; count = 0
check_num = -100000001
for i in range(n):

    if mylist[i] > check_num:
        if p > 1:
            p = 0
            continue
        if p == 1:
            p += 1
            check_num += k
        p += 1
        count += 1
        check_num = mylist[i] + k


print(count)

