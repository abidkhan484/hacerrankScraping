# Accepted
# Python 3

def quicksort_partition(li, end, start, total_swap):

    p = li[end-1]
    j = start-1
    for i in range(start, end-1):
        if li[i] < p:
            j += 1
            total_swap += 1
            li[i], li[j] = li[j], li[i]
    
    j += 1
    total_swap += 1
    li[end-1], li[j] = li[j], li[end-1]

#    print(total_swap, li)
    return j, total_swap

def quicksort(li, end, start=0, total_swap=0):

    position = 0
    if (end-start) > 1:
        position, total_swap = quicksort_partition(li, end, start, total_swap)
        total_swap = quicksort(li, position, start, total_swap)
        total_swap = quicksort(li, end, position+1, total_swap)

    return total_swap


def insertion_sort(li, n):
    total = 0
    for i in range(1, n):
        temp = li[i]
        j = i-1
        p = i
        while (j>=0):
            if (temp > li[j]):
                break
            else:
                #here total  is the variable that counts the swap
                total += 1
                li[p] = li[j]
                p -= 1
            j -= 1

        li[p] = temp

    return total


n = int(input().strip())
ar = list(map(int, input().split()))

pagli = []
pagli.extend(ar)
#quicksort_total is the variable which indicates the total swapping on the quicksort
quicksort_total = quicksort(ar, n)


#insertion_total is the variable which total swapping of the insertion sort
insertion_total = insertion_sort(pagli, n)

print(insertion_total - quicksort_total)

'''
input:
7
1 3 9 8 2 7 5

output:
1
'''

