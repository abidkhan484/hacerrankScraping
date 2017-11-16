# Accepted
# Python 3

class Solution:
    def __init__(self):
        self.mystack = list()
        self.myqueue = list()
        
    def pushCharacter(self, char):
        return self.mystack.append(char)

    def enqueueCharacter(self, char):
        return self.myqueue.append(char)

    def popCharacter(self):
        l = len(self.mystack)
        a = self.mystack[-1]
        self.mystack = self.mystack[:l-1]
        return a

    def dequeueCharacter(self):
        l = len(self.myqueue)
        a = self.myqueue[0]
        self.myqueue = self.myqueue[1:]
        return a
 
