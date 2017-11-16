# Wrong Answer
# Python 3

n = int(input().strip())


array = list(map(int, input().split()))
j = array[n-1]
for i in range(n-2, -1, -1):
    if (array[i] > j):
        array[i+1] = array[i]
        for p in range(n):
            print(array[p], end =' ')
    
    else:
        break
    print()

array[i+1] = j
for i in range(n):
    print(array[i], end=' ')

