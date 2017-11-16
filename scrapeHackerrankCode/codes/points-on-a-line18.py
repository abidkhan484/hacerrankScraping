# Wrong Answer
# Python 3

def horizontalVertical():
    for i in range(n-1):
        if li[i][0] != li[i+1][0]:
            break
    else:
        print('YES')
        return
    for i in range(n-1):
        if li[i][1] != li[i+1][1]:
            print('NO')
            return

n = int(input().strip())

li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

horizontalVertical()

