# Accepted
# Python 3

from collections import namedtuple
n = int(input().strip())

i = input().split()
res = namedtuple('res', '%s %s %s %s'%(i[0], i[1], i[2], i[3]))
avg = -1.0; total = 0

for i in range(n):
    temp = input().split()
    ido = res(temp[0], temp[1], temp[2], temp[3])
    temp = int(ido.MARKS)
    total = total + temp

print('%0.2f' %(total/n))

