# Wrong Answer
# Python 3

m, n = map(int, input().split())
ith = int(input().strip())

x = m/n
y = 1-x

total = 1
for i in range(4):
    total *= x
print(round(total*y, 3))

