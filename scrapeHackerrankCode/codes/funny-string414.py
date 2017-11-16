# Accepted
# Python 3

#!/bin/python3

n = int(input().strip())

for i in range(n):
    s = input().strip()

    # tmp list, to get the consequtive subtraction of the s list(string)
    s = list(s)
    tmp = []
    l = len(s)
    for j in range(1, l):
        temp = abs(ord(s[j]) - ord(s[j-1]))
        tmp.append(temp)

    # now reverse operation occer and check tmp with the reverse,
    # consequtive subtractions
    s.reverse()
    for j in range(1, l):
        temp = abs(ord(s[j]) - ord(s[j-1]))
        if temp != tmp[j-1]:
            break

    # if j is checked till the last, then print funny
    if j == l-1:
        print("Funny")
    else:
        print("Not Funny")

