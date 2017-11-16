# Wrong Answer
# Python 3

for _ in range(int(input().strip())):
    n = int(input().strip())
    i, divisor = 0, 9
    while True:
        if divisor//n==divisor/n:
            print(divisor)
            break
        if i&1:
            divisor -= 9
            divisor *= 10
        else:
            divisor += 9

        i += 1

