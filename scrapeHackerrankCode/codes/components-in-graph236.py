# Runtime Error
# Python 3

class DisjointSet:
    
    def __init__(self, data, head):
        self.data = data
        self.head = head

class Join(DisjointSet):

    def __init__(self):
        self.par_list = [None] * 15000

    def findHead(self, item, u):

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
            pagli = DisjointSet(a, a); bob = DisjointSet(b, a)
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


def main():

    edge = int(input().strip())
    pagli = Join()
    for _ in range(edge):
        x, y = map(int, input().split())
        pagli.join_two(x, y)

    li = []
    for i in range(15000):
        if pagli.par_list[i]:
            li.append(pagli.findHead(pagli.par_list[i], i))

    # i just write myself (collections.Counter) below
    dic = {}
    for i in range(len(li)):
            try:
                    dic[li[i]] += 1
            except:
                    dic[li[i]] = 1

    print(min(dic.values()), max(dic.values()))

main()


