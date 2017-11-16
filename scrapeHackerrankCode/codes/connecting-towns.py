# Wrong Answer
# Python 3

# this problem is still unsolved

def solve():

    n = int(input().strip())
    arr = [int(x) for x in input().split()]

    total = 1
    for i in range(n-1):
        total *= arr[i]
        if total > 12345678:
            total %= 1234567

    print(total)

def main():
    for _ in range(int(input().strip())):
        solve()

main()

