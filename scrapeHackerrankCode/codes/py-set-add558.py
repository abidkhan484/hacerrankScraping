# Accepted
# Python 3

n=int(input())
li=[]

for i in range(n):
    p=input().strip()
    li.append(p)

li=set(li)
print(len(li))

