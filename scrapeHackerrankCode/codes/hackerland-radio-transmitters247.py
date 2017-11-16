# Wrong Answer
# Python 3

n, k = [int(x) for x in input().split()] #8,2 #7, 2 #5, 1 #8, 2 
mylist = [int(x) for x in input().split()] #[7, 2, 4, 6, 5, 9, 12, 11] #[9, 5, 4, 2, 6, 15, 12] #[1,2,3,4,5] #[7, 2, 4, 6, 5, 9, 12, 11]

mylist.sort()

p = 1; count = 1
check_num = mylist[0] + k
for i in range(n):

    if mylist[i] > check_num:
        if p > 1:
            p = 1
            count += 1
            check_num = mylist[i] + k
        elif p == 1:
            if (check_num-k) == mylist[i-1]:
                check_num = mylist[i] + k
                p = 1
                count += 1
            else:
                p += 1
                check_num += k


print(count)


'''
input: 
5 1
1 2 3 4 5

output:
2

input:
8 2
7 2 4 6 5 9 12 11

output:
3
'''

