# Accepted
# Python 3

#!/bin/python3

import sys

def checkPos(startX, startY, count):

    li = []
    row=startX; col=startY
    while row:
        row -= 1
        if grid[row][col] == 'X':
            break
        elif grid[row][col] == '.':
            pass
        elif grid[row][col] < count:
            break
            
        grid[row][col] = count
        li.append((row, col))
    row = startX
    while col:
        col -= 1
        if grid[row][col] == 'X':
            break
        elif grid[row][col] == '.':
            pass
        elif grid[row][col] < count:
            break
        grid[row][col] = count
        li.append((row, col))
    col = startY
    while row < n-1:
        row += 1
        if grid[row][col] == 'X':
            break
        elif grid[row][col] == '.':
            pass
        elif grid[row][col] < count:
            break
        grid[row][col] = count
        li.append((row, col))
    row = startX
    while col < n-1:
        col += 1
        if grid[row][col] == 'X':
            break
        elif grid[row][col] == '.':
            pass
        elif grid[row][col] < count:
            break
        grid[row][col] = count
        li.append((row, col))
    
    return li


def minimumMoves(grid, startX, startY, goalX, goalY):

    count = 1
    grid[startX][startY] = 0
    mylist = checkPos(startX, startY, count)
    count = 2

    while mylist:

        if (goalX, goalY) in mylist:
            print(grid[goalX][goalY])
            return
        li = []
        while mylist:
            li.extend(checkPos(mylist[0][0], mylist[0][1], count))
            del mylist[0]

        mylist = li
        count += 1


if __name__ == "__main__":
    n = int(input().strip())
    grid = [list(input()) for _ in range(n)]
    startX, startY, goalX, goalY = map(int, input().split())
    result = minimumMoves(grid, startX, startY, goalX, goalY)


'''
10
..........
.X..XX...X
X.........
.X.......X
..........
........X.
.....X..XX
.....X.X..
..........
.....X..XX
9 1 9 6
'''

