# Wrong Answer
# Python 3

import re

p = input()
regex = r'[aeiouAEIOU]{2,}'

li = re.findall(regex,p)

if li:
    for i in li:
        print(i)
else:
    print('-1')

