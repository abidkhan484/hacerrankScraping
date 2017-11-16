# Runtime Error
# Python 3

import re

R = r'(\d)\1'
a = re.search(R,input())

print(a.lastindex)

