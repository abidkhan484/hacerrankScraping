# Terminated due to timeout
# Python 3

n = input().strip()

li = list(n)
i = 1; p = len(li); summation = 0
while i <= len(li):
    for j in range(p):
        tmp = ''
        for x in range(j, i+j):
            tmp += li[x]
        tmp = int(tmp)
        summation += tmp
        summation = (summation%(10**9+7))
    p -= 1; i += 1

print(summation)

