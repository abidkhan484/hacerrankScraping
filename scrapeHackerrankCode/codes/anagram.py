# Accepted
# Python 3

from collections import *

def anagram(st):
    l = len(st)
    if l//2 != l/2:
        return -1
    m = Counter(st[:l//2]); n = Counter(st[l//2:])
    return len(list(((m-n)+(n-m)).elements()))//2

n = int(input().strip())
for _ in range(n):
    st = input().strip()
    print(anagram(st))

