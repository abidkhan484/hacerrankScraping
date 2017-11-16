# Wrong Answer
# Python 3

n, k = [int(x) for x in input().split()]
mylist = [int(x) for x in input().split()]

mylist.sort()

i = 0; count = 1
check_num = mylist[0] + (2*k)
while i<n:

    if mylist[i] > check_num:
        count += 1
        check_num = mylist[i] + (2*k)

    i += 1

print(count)

