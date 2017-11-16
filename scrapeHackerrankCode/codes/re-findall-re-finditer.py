# Accepted
# Python 3

import re

p = input()
regex = r'(?=[^aeiouAEIOU]([aeiouAEIOU]{2,})[^aeiouAEIOU])'


li = re.findall(regex,p)

if li:
    for i in li:
        print(i)
else:
    print('-1')

