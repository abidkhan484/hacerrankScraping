# Accepted
# Python 3

def twoStrings(s1, s2):
    s1 = list(set(s1)); s2 = list(set(s2))
    for i in s1:
        for j in s2:
            if i==j:
                return 'YES'

    return 'NO'
    

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)

