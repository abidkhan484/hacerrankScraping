# Wrong Answer
# Python 3

import re


n = int(input().strip())
for _ in range(n):
    r = r'^[+-.]*[0-9]*[.]?[0-9]*$'
    a = input()
    if a=='0':
        print('False')
        continue
    x = re.search(r, a)
    print(bool(x))

