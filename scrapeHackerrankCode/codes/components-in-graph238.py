# Runtime Error
# Python 3

class DisjointSet:
    
    def __init__(self, data, head):
        self.data = data
        self.head = head

class Join:

    def __init__(self):
        self.par_list = []
        self.length = 0

    def findHead(self, item, u):

        if item.data==item.head:
            return u
        y = self.par_list.index(item.head)
        return Join.findHead(self, self.par_list[y], y)
        

    def join_two(self, a, b):

        u = -1; v = -1
        for i in range(self.length):
            if self.par_list[i].data == a:
                u = i
            if self.par_list[i].data == b:
                v = i

        if (u == -1) and (v == -1):
            a = DisjointSet(a, a); b = DisjointSet(b, a)
            self.par_list.append(a); self.par_list.append(b)
            self.length += 2

        elif (u != -1) and (v != -1):
            r = Join.findHead(self, self.par_list[u], u)
            self.par_list[r].head = self.par_list[v]

        else:
            if u != -1:
                p = Join.findHead(self, self.par_list[u], u)
                b = DisjointSet(b, self.par_list[p])
                self.par_list.append(b)

            else:
                p = Join.findHead(self, self.par_list[v], v)
                a = DisjointSet(a, self.par_list[p])
                self.par_list.append(a)

            self.length += 1


def main():

    edge = int(input().strip())
    pagli = Join()
    for _ in range(edge):
        x, y = map(int, input().split())
        pagli.join_two(x, y)

    li = []
    for i in range(pagli.length):
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

