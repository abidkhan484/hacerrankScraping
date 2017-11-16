# Wrong Answer
# Python 3

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    li=[]
    for i in arr:
        li.append(i)

    li.sort()
    n = n-1
    i = n-2
    
    while(i):
        if( li[i] != li[n] ):
            break
        i -= 1
            
    print(li[i])

