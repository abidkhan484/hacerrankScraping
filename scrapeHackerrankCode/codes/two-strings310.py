# Accepted
# Python 3

from collections import Counter

def twoStrings(s1, s2):
    s1 = list(Counter(s1).keys()); s2 = list(Counter(s2).keys())
    for i in s1:
        for j in s2:
            if i==j:
                return 'YES'

    return 'NO'
    

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)

