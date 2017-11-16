# Accepted
# Python 3

def counting_sort(li):
    return_list = [0] * 100
    for i in li:
        return_list[i] += 1

    for i in range(len(return_list)):
        n = return_list[i]
        while n > 0:
            print(i, end=' ')
            n -= 1

    return

n = int(input().strip())
li = list(map(int, input().split()))
counting_sort(li)

