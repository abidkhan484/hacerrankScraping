# Terminated due to timeout
# Python 3

mylist = []

for _ in range(int(input().strip())):
    temp = int(input().strip())
    mylist.append(temp)
    length = len(mylist)
    mylist.sort()
    if not (length & 1):
        l = (length-1) >> 1
        print('%.1lf' %((mylist[l]+mylist[l+1])/2))
    else:
        l = length >> 1
        print('%.1lf' %mylist[l])

