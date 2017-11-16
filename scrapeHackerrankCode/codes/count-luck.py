# Accepted
# Python 3

# this problem is still unsolved

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

def check_avail():

    row, column = map(int, input().split())
    arr = [[p for p in input().strip()] for i in range(row)]
    vstlist = [[False for p in range(column)] for i in range(row)]
    c_arr = [[0 for i in range(column)] for p in range(row)]
    k = int(input().strip())

    start = None; end = None
    for i in range(row):
        for j in range(column):
            if arr[i][j]=='*':
                end = (i,j)
            elif arr[i][j]=='M':
                start = (i,j)

        if start and end:
            break

    stack = []; curr=start; come_from=(-1,-1); poslist=[]
    while arr[curr[0]][curr[1]] != '*':

        if not vstlist[curr[0]][curr[1]]:
            mylist = move(arr, row, column, curr, come_from)
            vstlist[curr[0]][curr[1]] = True
        else:
            mylist = []
            
        length = len(mylist)
        if length==1:
            c_arr[curr[0]][curr[1]] = c_arr[come_from[0]][come_from[1]]
            come_from=curr
            curr = mylist[0]

        elif length > 1:
            c_arr[curr[0]][curr[1]] = c_arr[come_from[0]][come_from[1]] + 1
            come_from=curr
            while length-1:
                poslist.append(curr)
                length -= 1
            stack.extend(mylist)
            curr = stack.pop()       

        else:
            c_arr[curr[0]][curr[1]] = c_arr[come_from[0]][come_from[1]]
            come_from = poslist.pop()
            curr = stack.pop()
            c_arr[curr[0]][curr[1]] = c_arr[come_from[0]][come_from[1]]

        
    print('Impressed') if c_arr[come_from[0]][come_from[1]]==k else print('Oops!')


def main():
    for _ in range(int(input().strip())):
        check_avail()

main()

