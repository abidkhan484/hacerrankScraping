# Accepted
# Python 3

def find_lexicography():
    n = int(input().strip())
    grid = [[] for _ in range(n)]
    for i in range(n):
        pr = list(map(ord, input().strip()))
        pr.sort()
        grid[i].extend(pr)

    for i in range(n):
        j = 1
        while j < n:
            if grid[j][i] < grid[j-1][i]:
                return 'NO'
            j += 1
            
    return 'YES'
        

for i in range(int(input().strip())):
    print(find_lexicography())

