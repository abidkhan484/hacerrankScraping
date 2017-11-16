# Accepted
# Python 3

n = int(input())
s = set(map(int, input().split())) 

n = int(input())
for i in range(n):
    a=input().split()
    if (a[0]=='pop'):
        s.pop()
    elif (a[0]=='remove'):
        s.remove(int(a[1]))
    elif (a[0]=='discard'):
        s.discard(int(a[1]))


s=list(s)
n=0
for i in s:
    n += i

print(n)

