# Accepted
# Python 3

#!/bin/python3

import sys
import re

li = []
N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.search(r'@gmail\.com$', emailID):
        li.append(firstName)
        
li.sort()
for i in li:
    print(i)

