# Accepted
# Python 3

#!/bin/python3

import sys

n = int(input().strip())

first_input = set(input().strip())
for i in range(n-1):
    second_input = set(input().strip())
    first_input = first_input.intersection(second_input)

print(len(first_input))

