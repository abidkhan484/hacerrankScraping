# Accepted
# Python 3

def counting_sort(li):
    return_list = [0] * 100
    for i in li:
        return_list[i] += 1

    return return_list

n = int(input().strip())
li = list(map(int, input().split()))
print(*counting_sort(li))

