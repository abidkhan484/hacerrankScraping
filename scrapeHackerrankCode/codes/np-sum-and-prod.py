# Accepted
# Python 3

import numpy

n, m = map(int, input().split())
arr = [[int(p) for p in input().split()] for _ in range(n)]

print(numpy.prod(numpy.sum(arr, axis=0)))

