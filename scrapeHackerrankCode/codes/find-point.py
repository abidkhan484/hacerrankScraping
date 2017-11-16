# Accepted
# Python 3

def find_point(x1, y1, x2, y2):
    print((2*x2-x1), (2*y2-y1))

for _ in range(int(input().strip())):
    x1, y1, x2, y2 = input().split()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    find_point(x1, y1, x2, y2)

