# Accepted
# Python 3

from collections import *
a = Counter(input().strip())
b = Counter(input().strip())
c = a-b
d = b-a
e = c+d
print(len(list(e.elements())))
