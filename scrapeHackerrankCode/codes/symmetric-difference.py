# Accepted
# Python 3

p=int(input())
a=map(int, input().split())
a=set(a)
q=int(input())
b=map(int, input().split())
b=set(b)

temp=list(a-b)
temp.extend(b-a)
temp.sort()

for item in temp:
    print(item)
    
    

