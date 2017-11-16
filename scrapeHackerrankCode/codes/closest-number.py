# Wrong Answer
# Python 3

def closest_number(a, b, x):
    power = pow(a, b)
    differ = power%x
    if not differ:
        return power

    return min(power-differ, power-differ+x)

for _ in range(int(input().strip())):
    a, b, x = input().split()
    a, b, x = int(a), int(b), int(x)

    print(int(closest_number(a, b, x)))

