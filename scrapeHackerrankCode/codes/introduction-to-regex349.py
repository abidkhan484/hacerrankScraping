# Wrong Answer
# Python 3

import re


n = int(input().strip())
for _ in range(n):
    print(bool(re.search(r'^[+-.]*[0-9]*[.]?[0-9]*$', input())))

