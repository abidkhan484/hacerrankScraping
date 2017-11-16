# Accepted
# Python 3

import numpy

n, m = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.max(numpy.min(arr, axis=1)))

