# Wrong Answer
# Python 3

# this problem is still unsolved
# i just use CountLuck(hackerrank problem) (my) solution to solve this

def move(arr, row, column, curr_pos, come_from=None):

    li = []
    if ((curr_pos[0]+1) < row) and (arr[curr_pos[0]+1][curr_pos[1]] != 'X'):
        li.append((curr_pos[0]+1, curr_pos[1]))

    if ((curr_pos[1]+1) < column) and (arr[curr_pos[0]][curr_pos[1]+1] != 'X'):
        li.append((curr_pos[0], curr_pos[1]+1))

    if ((curr_pos[0]-1) >= 0) and (arr[curr_pos[0]-1][curr_pos[1]] != 'X'):
        li.append((curr_pos[0]-1, curr_pos[1]))

    if ((curr_pos[1]-1) >= 0) and (arr[curr_pos[0]][curr_pos[1]-1] != 'X'):
        li.append((curr_pos[0], curr_pos[1]-1))

    if come_from in li:
        idx = li.index(come_from)
        del li[idx]        
    
    return li


def countdown(prev, c_arr, curr, come_from):

    pagli = prev[come_from[0]][come_from[1]]
    if ((curr[0]==come_from[0]) and (come_from[0]!=pagli[0])) \
       and ((curr[1]!=come_from[1]) and (come_from[1]==pagli[1])):

        c_arr[curr[0]][curr[1]] = c_arr[come_from[0]][come_from[1]] + 1
        return

    if ((pagli[0]==come_from[0]) and (pagli[0]!=curr[0])) \
         and ((pagli[1]!=come_from[1]) and (curr[1]==come_from[1])):
        c_arr[curr[0]][curr[1]] = c_arr[come_from[0]][come_from[1]] + 1
        return
    c_arr[curr[0]][curr[1]] = c_arr[come_from[0]][come_from[1]]
    return


row = int(input().strip())
column = row
arr = [[p for p in input().strip()] for i in range(row)]
vstlist = [[False for p in range(column)] for i in range(row)]
c_arr = [[1 for i in range(column)] for p in range(row)]
prev = [[None for i in range(column)] for p in range(row)]

x, y, e, f = map(int, input().split())
start = (x,y); end = (e,f)

stack = []; curr=start; come_from=start; poslist=[]; prev[curr[0]][curr[1]] = curr
while curr != end:

    if not vstlist[curr[0]][curr[1]]:
        mylist = move(arr, row, column, curr, come_from)
        vstlist[curr[0]][curr[1]] = True
    else:
        mylist = []
        
    length = len(mylist)
    if length==1:
        come_from=curr
        curr = mylist[0]

    elif length > 1:
        come_from=curr
        while length-1:
            poslist.append(curr)
            length -= 1
        stack.extend(mylist)
        curr = stack.pop()       

    else:
        come_from = poslist.pop()
        curr = stack.pop()
    
    prev[curr[0]][curr[1]] = come_from
    countdown(prev, c_arr, curr, come_from)
    
print(c_arr[curr[0]][curr[1]])


