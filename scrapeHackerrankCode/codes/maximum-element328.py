# Accepted
# Python 3

class Stack:
    def __init__(self):
        self.my_list = []
        self.item_list = []

    def push(self, item):
        self.my_list.append(item)
        if self.item_list:
            if self.item_list[-1] <= item:
                self.item_list.append(item)

        else:
            self.item_list.append(item)
        return

    def pop(self):
        pop_item = self.my_list.pop()
        if pop_item == self.item_list[-1]:
            self.item_list.pop()
        return

    def maxim(self):
        return self.item_list[-1]


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

