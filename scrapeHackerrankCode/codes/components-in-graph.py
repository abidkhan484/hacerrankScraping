# Accepted
# Python 3

class DisjointSet:
    
    def __init__(self, data, head):
        self.data = data
        self.head = head

class Join(DisjointSet):

    def __init__(self):
        self.par_list = [None] * 30001

    def findHead(self, item, u):

        '''
        y = u
        while True:
            item = self.par_list[y-1]
            if item.data==item.head:
                return y
            try:
                y = item.head.data
            except:
                y = item.head
            y -= 1
        '''

        if item.data==item.head:
            return u
        try:
            y = item.head.data
        except:
            y = item.head
        return Join.findHead(self, self.par_list[y-1], y-1)
        

    def join_two(self, a, b):

        if self.par_list[a-1]:
            u = a-1
        else:
            u = -1

        if self.par_list[b-1]:
            v = b-1
        else:
            v = -1
            
        if (u == -1) and (v == -1):
            pagli = DisjointSet(a, a); bob = DisjointSet(b, pagli)
            self.par_list[a-1] = pagli; self.par_list[b-1] = bob

        elif (u != -1) and (v != -1):
            p = Join.findHead(self, self.par_list[v], v)
            r = Join.findHead(self, self.par_list[u], u)
            if p != r:
                self.par_list[r].head = self.par_list[v]

        else:
            if u != -1:
                p = Join.findHead(self, self.par_list[u], u)
                bob = DisjointSet(b, self.par_list[p])
                self.par_list[b-1] = bob

            else:
                p = Join.findHead(self, self.par_list[v], v)
                bob = DisjointSet(a, self.par_list[p])
                self.par_list[a-1] = bob

def find(item, li, y, i):

    if item.data==item.head:
        li[i] = y
        return

    try:
        y = item.head.data
    except:
        y = item.head

    if li[y-1] != -1:
        li[i] = li[y-1]
        return

    return find(pagli.par_list[y-1], li, y-1, i)

#def main():

edge = int(input().strip())
pagli = Join()
for _ in range(edge):
    x, y = map(int, input().split())
    pagli.join_two(x, y)

li = [-1]*30001
for i in range(30001):
    if pagli.par_list[i]:
        find(pagli.par_list[i], li, i, i)

# i just write myself (collections.Counter) below
dic = {}
for i in range(len(li)):
        try:
                dic[li[i]] += 1
        except:
                dic[li[i]] = 1
del dic[-1]

print(min(dic.values()), max(dic.values()))

#main()

