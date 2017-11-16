# Wrong Answer
# Python 3

import re

R = r'(\d)\1'
a = re.search(R,input())

if a:
    print(a.lastindex)
else:
    print(-1)

