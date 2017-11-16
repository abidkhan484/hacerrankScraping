# Wrong Answer
# Python 3

#!/bin/python3

import sys

n = int(input().strip())
li = [input().strip() for i in range(n)]

tmp = []
for i in range(n):
    count = 1; j = i+1

    if li[i] != '':
        while (j < n):
            if li[i] == li[j]:
                li[j] = ''
                count += 1
            j += 1
    else:
        break

    tmp.append(count)

print(len(tmp))
for i in tmp:
    print(i, end=' ')

