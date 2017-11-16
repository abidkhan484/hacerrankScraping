# Accepted
# Python 3

from collections import deque

d = deque()
n=int(input().strip())

for i in range(n):
    temp = input().split()
    if temp[0] == 'append':
        d.append(temp[1])
    elif temp[0] == 'appendleft':
        d.appendleft(temp[1])
    elif temp[0] == 'pop':
        d.pop()
    elif temp[0] == 'popleft':
        d.popleft()
        
for i in d:
    print(i, end=' ')
