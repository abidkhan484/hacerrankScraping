# Accepted
# Python 3

def make_multi(i):
    li = []
    while i:
        if i%2==1:
            li.append(9)
        else:
            li.append(0)
        i //= 2
    li.reverse()

    total = 0
    for i in li:
        total = total*10 + i
    return total

li = []
for i in range(1, 10001):
    li.append(make_multi(i))

#print(li)


for _ in range(int(input().strip())):
    n = int(input().strip())
    i = 0
    for i in li:
        if not (i%n):
            print(i)
            break
        

