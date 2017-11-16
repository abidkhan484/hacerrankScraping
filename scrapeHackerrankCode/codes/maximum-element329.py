# Terminated due to timeout
# Python 3

class Stack:
    def __init__(self):
        self.my_list = []

    def push(self, item):
        return self.my_list.append(item)

    def pop(self):
        self.my_list.pop()
        return

    def maxim(self):
        return max(self.my_list)

s = Stack()

n = int(input().strip())

for i in range(n):
    st = input().split()
    if st[0] == '1':
        s.push(int(st[1]))
    elif st[0] == '2':
        s.pop()
    elif st[0] == '3':
        print(s.maxim())

