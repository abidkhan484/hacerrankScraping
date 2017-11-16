# Wrong Answer
# Python 3

#!/bin/python3

import sys


N = int(input().strip())

if(N%2==1):
    print("Weird")
    
elif(N%2==0 & (N>5) & (N<21)):    
    print("Weird")
else:
    print("Not Weird")
