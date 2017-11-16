# Accepted
# Python 3

n=int(input())
a=map(int, input().split())
a=set(a)

m=int(input())
b=map(int, input().split())
b=set(b)

print(len(a.symmetric_difference(b)))

