# Accepted
# Python 3

#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    l = len(grades)
    for i in range(l):
        if (((grades[i]%5)==0) or (grades[i]<38)):
            continue
        else:
            p = (grades[i]//5)+1
            if ((p*5)-grades[i] < 3):
                grades[i] = p*5

    return grades
    
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
for i in grades:
    print(i)

