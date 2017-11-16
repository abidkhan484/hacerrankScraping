# Accepted
# Python 3

import numpy

n, m, p = map(int, input().split())

ar = numpy.array([[int(r) for r in input().split()] for _ in range(n)])
arr = numpy.array([[int(r) for r in input().split()] for _ in range(m)])


print(numpy.concatenate((ar,arr), axis=0))

