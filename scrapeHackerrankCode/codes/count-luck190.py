# Terminated due to timeout
# Python 3

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

    stack = []; curr=start; come_from=None; poslist=[]; count=0
    while arr[curr[0]][curr[1]] != '*':
        mylist = move(arr, row, column, curr, come_from)

        if len(mylist)==1:
            come_from=curr
            curr = mylist[0]
        elif len(mylist) > 1:
            come_from=curr
            poslist.append(curr)
            stack.extend(mylist)
            curr = stack.pop()
            count += 1
        else:
            come_from = poslist.pop()
            curr = stack.pop()

    print('Impressed') if count==k else print('Oops!')

def main():
    for _ in range(int(input().strip())):
        check_avail()

main()

