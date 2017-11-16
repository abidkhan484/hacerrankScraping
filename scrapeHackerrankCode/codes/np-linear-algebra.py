# Accepted
# Python 3

import numpy

n = int(input().strip())
arr = numpy.array([[float(p) for p in input().split()] for _ in range(n)])

print(numpy.linalg.det(arr))

