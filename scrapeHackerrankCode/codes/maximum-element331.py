# Terminated due to timeout
# Python 3

n = int(input().strip())

li = []
for i in range(n):
    st = input().split()
    if st[0] == '1':
        li.append(int(st[1]))
    elif st[0] == '2':
        li.pop()
    elif st[0] == '3':
        print(max(li))

