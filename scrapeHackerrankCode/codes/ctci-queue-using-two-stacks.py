# Accepted
# Python 3

class MyQueue(object):
    def __init__(self):
        self.mylist = []
    
    def peek(self):
        return self.mylist[0]
        
    def pop(self):
        return self.mylist.pop(0)
        
    def put(self, value):
        return self.mylist.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())


