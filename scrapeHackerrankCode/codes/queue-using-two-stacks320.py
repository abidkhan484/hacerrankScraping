# Accepted
# Python 3

mylist = []

n = int(input().strip())
for _ in range(n):
    tmp = input().split()
    if tmp[0]=='1':
        mylist.append(int(tmp[1]))
    elif tmp[0]=='2':
        mylist = mylist[1:]
    else:
        print(mylist[0])

