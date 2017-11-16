# Accepted
# Python 3

n = int(input().strip())

my_str = ''
stack = [my_str]
for _ in range(n):
    t = input().split()
    if t[0] == '1':
        my_str += t[1]
        stack.append(my_str)
    elif t[0] == '2':
        my_str = my_str[:len(my_str)-int(t[1])]
        stack.append(my_str)
    elif t[0] == '3':
        print(my_str[int(t[1])-1])
    else:
        stack.pop()
        my_str = stack[-1]

