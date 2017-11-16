# Accepted
# Python 3

class Stack:

    def __init__(self):
        self.my_list = []


    def push(self, item):
        self.my_list.append(item)
        return

    def pop(self):
        return self.my_list.pop()


    def matching_par(self, st):
        length = len(st)
        if length//2 != length/2:
            return False
        my_dict = {'(': ')', '{':'}', '[':']'}

        while st:
            tmp = st[0]
            if tmp in my_dict.keys():
                Stack.push(self, tmp)
            else:
                try:
                    item = Stack.pop(self)
                    if my_dict[item] != tmp:
                        return False
                except IndexError:
                    return False
            st = st[1:]

        if self.my_list:
            return False

        return True
        

s = Stack()

n = int(input().strip())
for i in range(n):
    st = input().strip()
    s.my_list = []
    if s.matching_par(st):
        print('YES')
    else:
        print('NO')



'''#!/bin/python3

import sys

def par_checker(s):
    length = len(s)
    if not length//2==length/2:
        return False
    l = ['(', '{', '[']
    r = [')', '}', ']']

    li = []
    for i in s:
        if i in r:
            break
        li.append(i)

    for i in range(length//2):
        for j in range(3):
            if l[j] == li[i]:
                break

        if not s[length-i-1]==r[j]:
            break

    else:
        return True

    return False


t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    if par_checker(s) is True:
        print('YES')
    else:
        print('NO')
'''

