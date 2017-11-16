# Accepted
# Python 3

    def insert(self,head,data): 
    #Complete this method
        current = head
        if head is None:
            head = Node(data)
        else:
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return head
                

