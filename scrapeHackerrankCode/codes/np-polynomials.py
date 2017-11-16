# Accepted
# Python 3

import numpy

arr = numpy.array([float(p) for p in input().split()])
print(numpy.polyval(arr, int(input().strip())))

