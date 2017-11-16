# Accepted
# Python 3

import re

R = r'^[789]\d{9}$'

for i in range(int(input().strip())):
    if bool(re.match(R, input())):
        print('YES')
    else:
        print('NO')

