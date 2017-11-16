# Accepted
# Python 3

n=int(input())
a=map(int, input().split())
a=set(a)
p=0

n=int(input())
for i in range(n):
    li= input().split()
    if(li[0]=='intersection_update'):
        b=map(int, input().split())
        b=set(b)
        a.intersection_update(b)
    elif(li[0]=='update'):
        b=map(int, input().split())
        b=set(b)
        a.update(b)
    elif(li[0]=='difference_update'):
        b=map(int, input().split())
        b=set(b)
        a.difference_update(b)
    elif(li[0]=='symmetric_difference_update'):
        b=map(int, input().split())
        b=set(b)
        a.symmetric_difference_update(b)

a=list(a)
n=0
for i in a:
    n += i
print(n)

