# Accepted
# Python 3

def findHead(num):

    if type(par_list[num]) == list:
        return num

    return findHead(par_list[num])

def join_two(a, b):

    u = type(par_list[a]); v = type(par_list[b])
    if (u==list) and (v==list):
        p = a; q = b
        l = len(par_list[q]); le = len(par_list[p])
        if le > l:
            par_list[p].extend(par_list[q])
            for i in range(1, l):
                tmp = par_list[q][i]
                par_list[tmp] = p
            par_list[q] = p
        else:
            par_list[q].extend(par_list[p])
            for i in range(1, le):
                tmp = par_list[p][i]
                par_list[tmp] = q
            par_list[p] = q

    elif (u != list) and (v != list):
        if par_list[a]==par_list[b]:
            return
        p = findHead(par_list[a]); q = findHead(par_list[b])
        l = len(par_list[q]); le = len(par_list[p])
        if le > l:
            par_list[p].extend(par_list[q])
            for i in range(1, l):
                tmp = par_list[q][i]
                par_list[tmp] = p
            par_list[q] = p
        else:
            par_list[q].extend(par_list[p])
            for i in range(1, le):
                tmp = par_list[p][i]
                par_list[tmp] = q
            par_list[p] = q

    elif (u == list) and (v != list):
        if par_list[b]==a:
            return
        q = findHead(par_list[b]); p = a
        l = len(par_list[q]); le = len(par_list[p])
        if le > l:
            par_list[p].extend(par_list[q])
            for i in range(1, l):
                tmp = par_list[q][i]
                par_list[tmp] = p
            par_list[q] = p
        else:
            par_list[q].extend(par_list[p])
            for i in range(1, le):
                tmp = par_list[p][i]
                par_list[tmp] = q
            par_list[p] = q

    elif (u != list) and (v == list):
        if par_list[a]==b:
            return
        q = b; p = findHead(par_list[a])
        l = len(par_list[q]); le = len(par_list[p])
        if le > l:
            par_list[p].extend(par_list[q])
            for i in range(1, l):
                tmp = par_list[q][i]
                par_list[tmp] = p
            par_list[q] = p
        else:
            par_list[q].extend(par_list[p])
            for i in range(1, le):
                tmp = par_list[p][i]
                par_list[tmp] = q
            par_list[p] = q        

node, edge = map(int, input().split())

par_list = [[p] for p in range(node)]

for _ in range(edge):
    tmp = input().split()
    if tmp[0]=='Q':
        u = findHead(int(tmp[1])-1)
        print(len(par_list[u]))

    else:
        if tmp[1]==tmp[2]:
            continue
        join_two(int(tmp[1])-1, int(tmp[2])-1)

