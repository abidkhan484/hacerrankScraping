# Accepted
# Python 3

m, n = map(int, input().split())
ith = int(input().strip())

# x is the probability to be the defect
# and y is perfect
x = m/n
y = 1-x

# according to the problem, first 4 are perfect
# and the 5th one will be defect 
total = 1
for i in range(4):
    total *= y
print(round(total*x, 3))

