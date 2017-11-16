# Accepted
# Python 3

if __name__ == '__main__':

    li = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name, score])
    li.sort()
    l = len(li)
    vir_li = []
    #vir_li = [vir_li.append(li[s][1])   for s in range(le)]
    for s in range(l):
        vir_li.append(li[s][1])

    vir_li.sort()
    s = 0
    le = 1

    while(le):
        if (vir_li[le] != vir_li[s]):
            break
        else:
            le += 1

    for s in range(l):
        if (vir_li[le]==li[s][1]):
            print(li[s][0])
            

