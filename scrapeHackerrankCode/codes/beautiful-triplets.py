# Terminated due to timeout
# Python 3

n, d = input().split()
n, d = int(n), int(d)
count = 0

li = [int(p) for p in input().split()]

for i in range(n-2):
    temp = li[i]
    j = i+1
    while j<n:
        if li[j] == (temp+d):
            temp += d
            if temp == (li[i]+d+d):
                count += 1
                break

        j += 1

print(count)

