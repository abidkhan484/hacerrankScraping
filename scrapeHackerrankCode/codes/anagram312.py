# Accepted
# Python 3

import string

s = list(string.ascii_lowercase)
def test_anagram(st):
    l = len(st)
    if l//2 != l/2:
        return -1
    m = st[:(l//2)]; n = st[(l//2):]
    m.lower(); n.lower()
    mList = [0] * 26
    nList = [0] * 26

    for i in range(l//2):
        if m[i] in s:
            index = s.index(m[i])
            mList[index] += 1


    for i in range(l//2):
        if n[i] in s:
            index = s.index(n[i])
            nList[index] += 1

    count = 0
    for i in range(26):
        if mList[i] == nList[i]:
            continue
        else:
            count += (max(mList[i], nList[i]) - min(mList[i], nList[i]))
    return count//2

n = int(input().strip())
for _ in range(n):
    st = input().strip()
    print(test_anagram(st))

