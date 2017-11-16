# Accepted
# Python 3

#!/bin/python3

import sys


n = int(input().strip())

bin_val = bin(n)[2:]
x = len(bin_val)
count1, count2 = 0, 0
while(x):
    if bin_val[x-1] is '1':
        count1+=1
    else:
        if(count2 < count1):
            count2=count1
        count1=0
    x-=1
if (count2>count1):
    print(count2)
else:
    print(count1)


