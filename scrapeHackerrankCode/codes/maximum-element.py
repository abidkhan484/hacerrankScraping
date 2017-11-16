# Accepted
# Python 3

my_list = []
item_list = []

def push(item):
    my_list.append(item)
    if item_list:
        if item_list[-1] <= item:
            item_list.append(item)

    else:
        item_list.append(item)
    return

def pop():
    pop_item = my_list.pop()
    if pop_item == item_list[-1]:
        item_list.pop()
    return

def maxim():
    return item_list[-1]


n = int(input().strip())

for i in range(n):
    st = input().split()
    if st[0] == '1':
        push(int(st[1]))
    elif st[0] == '2':
        pop()
    elif st[0] == '3':
        print(maxim())

