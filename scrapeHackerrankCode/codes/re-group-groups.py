# Accepted
# Python 3

import re

R = r'([\da-zA-Z])\1'
a = re.search(R,input())

if a:
    print(a.group()[0])
else:
    print(-1)

