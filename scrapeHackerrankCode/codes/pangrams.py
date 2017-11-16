# Accepted
# Python 3

#!/bin/python3

import sys

if len(set(input().lower().strip())) != 27:
    print("not pangram")
else:
    print("pangram")

