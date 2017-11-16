# Accepted
# Python 3

import numpy

n, m = map(int, input().split())
ar = numpy.array([[int(p) for p in input().split()] for _ in range(n)])
arr = numpy.array([[int(p) for p in input().split()] for _ in range(n)])

print(numpy.array(numpy.add(ar, arr), dtype=numpy.int))
print(numpy.array(numpy.subtract(ar, arr), dtype=numpy.int))
print(numpy.array(numpy.multiply(ar, arr), dtype=numpy.int))
print(numpy.array(numpy.divide(ar, arr), dtype=numpy.int))
print(numpy.array(numpy.mod(ar, arr), dtype=numpy.int))
print(numpy.array(numpy.power(ar, arr), dtype=numpy.int))


