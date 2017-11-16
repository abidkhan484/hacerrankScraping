# Accepted
# Python 3

n, k = input().split()
n, k = int(n), int(k)

t = [int(p) for p in input().split()]

page = 1; count = 0
for i in range(n):
    var = t[i]
    j = 0
    while j < var:
        temp = j+k
        if temp > var:
            temp = var
            
        if (j < page) and (temp >= page):
            count += 1
            page += 1
        else:
            page += 1

        j = temp

print(count)

