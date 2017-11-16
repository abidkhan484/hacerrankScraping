# Accepted
# Python 3

#!/bin/python3

import sys

def test_arr(arr, i, j):
    summation=0
    for p in range(3):
        t=j
        for q in range(3):
            if p is 1:
                summation += arr[i][t+1]
                break
            else:
                summation += arr[i][t]
                t+=1
        i+=1

    return summation
    

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

temp=-10000
for i in range(4):
    for j in range(4):
        tempo=test_arr(arr, i, j)
        if (temp<tempo):
            temp=tempo

print(temp)

