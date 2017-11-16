# Accepted
# Python 3

for _ in range(int(input().strip())):
    n = int(input().strip())
    i = 1
    while True:
        p = int(bin(i)[2:].replace('1', '9'))
        if not (p%n):
            print(p)
            break
        i += 1

