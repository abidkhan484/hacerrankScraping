# Accepted
# Python 3

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    li=[]
    for i in arr:
        li.append(i)

    li.sort()

    i = n-2
    n = n-1
    while (i):        
        if li[i] is li[n]:
            i -= 1

        else:
            break

    print(li[i])

