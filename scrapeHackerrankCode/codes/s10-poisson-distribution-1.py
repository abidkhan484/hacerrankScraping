# Accepted
# Python 3

from math import factorial

p = float(input().strip())
r = float(input().strip())

ans = ((p**r)*(2.71828**(-p)))/factorial(r)
print('%.3lf'%ans)

