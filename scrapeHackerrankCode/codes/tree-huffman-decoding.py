# Accepted
# Python 2

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    string = ''; curr = root; i=0; le = len(s)
    while i < le:
        if s[i]=='1':
            curr = curr.right
        else:
            curr = curr.left
        
        if curr.data != '\0':
            string += curr.data
            curr = root
        
        i += 1
        
    print string
        
    return string

