# Terminated due to timeout
# Python 3

#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
count = 0
maxim = -1
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)
    
i = 0
while i < n-1:

    k = i+1
    while k < n:
        
        j = 0; tmp = 0
        while j < m:
            if (topic[i][j]=='1') or (topic[k][j]=='1'):                
                tmp += 1
            j += 1

        if tmp > maxim:
            maxim = tmp
            count = 1

        elif tmp==maxim:
            count +=1

        k += 1

    i += 1


print(maxim, count, sep='\n')

