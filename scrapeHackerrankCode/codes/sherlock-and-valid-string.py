# Wrong Answer
# Python 3

import collections

n = input().strip()
#pr variable makes a dictionary what are the elements and how much time occers
pr = collections.Counter(n)
#a var inputs the keys on a list
a = list(pr.keys())

# count var checks the required conditions
# y is the var that checks what are the values
count = 0; y = pr[a[0]]

for i in a:
    if pr[i] != y:
        count += 1
        if count > 1:
            print('NO')
            break

else:
    print('YES')

