# Terminated due to timeout
# Python 3

class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def maxim(self):
        return max(self.items)

s = stack()
n = int(input().strip())

for _ in range(n):
    i = input().split()
    if i[0]=='1':
        s.push(int(i[1]))
    elif i[0]=='2':
        s.pop()
    else:
        print(s.maxim())

