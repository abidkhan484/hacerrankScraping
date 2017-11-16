# Terminated due to timeout
# Python 3

def make_array():
    num = 10**6 + 1
    ar = [0] * num

    ar[1] = 1; ar[2]=2; ar[3]=3
    for i in range(2, 1001):
        j = 2*i; c = ar[i]+1; mistake = i**2
        if mistake > num:
            mistake = num
        while j <= mistake:
            if not ar[j]:
                ar[j] = c
            else:
                if c < ar[j]:
                    ar[j] = c
            j += i

        for p in range(i+1, mistake):
            if not ar[p]:
                ar[p] = ar[p-1] + 1

    return ar


ar = make_array()
for _ in range(int(input().strip())):
    i = int(input().strip())
    print(ar[i])

