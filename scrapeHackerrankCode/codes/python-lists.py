# Accepted
# Python 3

if __name__ == '__main__':
    N = int(input())
    li = []

    for i in range(N):
        vir_li = input().split()

        if (vir_li[0]=='print'):
            print(li)

        elif (vir_li[0]=='reverse'):
            li.reverse()

        elif (vir_li[0]=='sort'):
            li.sort()

        elif (vir_li[0]=='pop'):
            li.pop()

        elif (vir_li[0]=='append'):
            li.append( int(vir_li[1]) )

        elif (vir_li[0]=='remove'):
            li.remove(int(vir_li[1]))

        elif (vir_li[0]=='insert'):
            li.insert(int(vir_li[1]), int(vir_li[2]))
            

