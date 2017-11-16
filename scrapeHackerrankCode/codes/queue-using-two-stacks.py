# Terminated due to timeout
# Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:        
    def enqueue(self, head, item):
        if not head:
            return Node(item)
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = Node(item)
        return head


n = int(input().strip())
q = queue()
head = None

for _ in range(n):
    tmp = input().split()
    if tmp[0]=='1':
        head = q.enqueue(head, int(tmp[1]))
    elif tmp[0]=='2':
        head = head.next
    else:
        print(head.data)

