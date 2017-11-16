# Wrong Answer
# Python 3

class Stack:

    def __init__(self):
        self.my_list = []
        return
    '''
    def is_empty(self):
        return self.my_list==[]
    '''


    def is_empty(self):
        if not self.my_list:
            return True
        else:
            return False

    def push(self, item):
        self.my_list.append(item)
        return

    def size(self):
        return len(self.my_list)

    def pop(self):
        return self.my_list.pop()

    def peek(self):
        return self.my_list[-1]

    def rev_string(self, my_str):
        
        if len(my_str)==1:
            return my_str[-1]

        return my_str[-1] + Stack.rev_string(self, my_str[:-1])

    def rev_my_list(self):
        for i in range(len(self.my_list)):
            if str(self.my_list[i]) == self.my_list[i]:
                rev = Stack.rev_string(self, self.my_list[i])
                self.my_list[i] = rev
                
            else:
                continue

        return self.my_list
        

s = Stack()
#print(s.is_empty())
#s.push(4)
#s.push('dog')
#print(s.peek())
#s.push(True)
#print(s.size())
#print(s.is_empty())
#s.push(8.4)
#print(s.pop()); print(s.size())
#print(s.my_list)
#print(s.rev_my_list())

n = int(input().strip())
for i in range(n):
    elem = input().split()
    if elem[0]=='1':
        s.push(elem[1])
    elif elem[0]=='2':
        s.pop()
    else:
        print(max(s.my_list))

