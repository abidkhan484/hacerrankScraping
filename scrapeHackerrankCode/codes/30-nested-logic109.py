# Wrong Answer
# Python 3

rday, rmonth, ryear = [int(p) for p in input().split()]
pday, pmonth, pyear = [int(p) for p in input().split()]

total = 0
if (pyear >= ryear):
    if (pmonth >= rmonth):
        if rday > pday:
            total = 15*(rday-pday)
    else:
        total = 500*(rmonth-pmonth)
else:
    total = 10000

print(total)    

