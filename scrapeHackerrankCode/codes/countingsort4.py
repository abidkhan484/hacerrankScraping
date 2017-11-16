# Wrong Answer
# Python 3

def counting_sort(li, last):
    mylist = []
    for i in range(100):
        if li:
            mylist.extend(li[i])

    for i in mylist:
        if i in last:
            print(i, end=' ')
        else:
            print('-',end=' ')
    
    return mylist


n = int(input().strip())
mylist = [[] for i in range(100)]
last_items = []

for i in range(n):
    m, a = input().split()
    m = int(m)
    mylist[m].append(a)
    if ((n//2) <= i):
        last_items.append(a)

counting_sort(mylist, last_items)

