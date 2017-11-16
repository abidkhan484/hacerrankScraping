# Accepted
# Python 3

import numpy

n = int(input().strip())
a = numpy.array([[int(p) for p in input().split()] for _ in range(n)])
b = numpy.array([[int(p) for p in input().split()] for _ in range(n)])

print(numpy.dot(a,b))

