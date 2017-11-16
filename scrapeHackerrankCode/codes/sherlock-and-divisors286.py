# Wrong Answer
# Python 3

def check_divisor(n, i=0):
    if n&1:
        return i
    return check_divisor(n//2, i+1)

for _ in range(int(input().strip())):
    print(check_divisor(int(input().strip())))   
