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
        return self.mystack.pop()

    def dequeueCharacter(self):
        return self.myqueue.pop(0)
 
