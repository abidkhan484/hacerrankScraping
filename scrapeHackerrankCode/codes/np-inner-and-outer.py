# Accepted
# Python 3

import numpy

ar = numpy.array([int(p) for p in input().split()])
arr = numpy.array([int(p) for p in input().split()])

print(numpy.inner(ar, arr))
print(numpy.outer(ar, arr))

