# Wrong Answer
# Python 3

def completeTheRow(i, p):
    
    for j in range(p, -1, -1):
        n[i].append(n[i][j])

# n is a two-dimentional array which i used
# for memorization of pascal triangle
# range is <1000 as the constraints
n = [[1] for _ in range(1000)]
# just manually add the second row of n
n[1].append(1)

for i in range(2, 1000):

    for j in range(i//2):
        n[i].append(n[i-1][j]+n[i-1][j+1])

    if not (i&1):
        completeTheRow(i, len(n[i])-2)
    else:
        completeTheRow(i, len(n[i])-1)
        
for _ in range(int(input().strip())):
    print(*n[int(input().strip())])

