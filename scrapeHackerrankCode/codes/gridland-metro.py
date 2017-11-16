# Wrong Answer
# Python 3

def checkPrev(num):
    
    for i in range(len(li)):
        if li[i][0]==num:
            return i
    return -1

n, m, k = map(int, input().split())

total = n*m; li = []
for i in range(k):
    tmp = list(map(int, input().split()))
    che = checkPrev(tmp[0])

    if che == -1:
        total -= (tmp[2]-tmp[1]+1)
        li.append(tmp)
    else:
        if (li[che][1] <= tmp[1]) and (li[che][2] < tmp[2]):
            t = tmp[2] - li[che][2]
            total -= t
            li[che][2] += t

        elif (li[che][1] > tmp[1]) and (li[che][2] >= tmp[2]):
            t = li[che][1] - tmp[1]
            total -= t
            li[che][1] -= t

        elif (li[che][1] > tmp[1]) and (li[che][2] < tmp[2]):
            t = tmp[2] - li[che][2]
            total -= t
            li[che][2] += t
            t = li[che][1] - tmp[1]
            total -= t
            li[che][1] -= t
            
print(total)

