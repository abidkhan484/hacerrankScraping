# Accepted
# Python 3

import re

q = input()
p = input()
R = r'%s' %p    # Do not delete 'r'.
    


if not bool(re.search(R, q)):
    print('(-1, -1)')
else:
    c, d = 0, 0
    l = len(p)
    while q:
        a = re.search(R, q)
        if not a:
            break
        i = a.start()
        c = c+i
        d = c+l-1
        print('(%d, %d)'%(c,d))
        c += 1

        q = q[(i+1):]

