# Wrong Answer
# Python 3

#!/bin/python3

import sys

def checkPos(startX, startY):

    li = []
    row=startX; col=startY
    while row:
        row -= 1
        if grid[row][col] != '.':
            break
        grid[row][col] = -1
        li.append((row, col))
    row = startX
    while col:
        col -= 1
        if grid[row][col] != '.':
            break
        grid[row][col] = -1
        li.append((row, col))
    col = startY
    while row < n-1:
        row += 1
        if grid[row][col] != '.':
            break
        grid[row][col] = -1
        li.append((row, col))
    row = startX
    while col < n-1:
        col += 1
        if grid[row][col] != '.':
            break
        grid[row][col] = -1
        li.append((row, col))
    
    return li


def minimumMoves(grid, startX, startY, goalX, goalY):

    count = 1
    grid[startX][startY] = -1
    mylist = checkPos(startX, startY)

    while mylist:
        if (goalX, goalY) in mylist:
            print(count)
            return
        li = []
        while mylist:
            li.extend(checkPos(mylist[0][0], mylist[0][1]))
            del mylist[0]

        mylist = []
        mylist.extend(li)
        count += 1


if __name__ == "__main__":
    n = int(input().strip())
    grid = [list(input()) for _ in range(n)]
    startX, startY, goalX, goalY = map(int, input().split())
    result = minimumMoves(grid, startX, startY, goalX, goalY)


