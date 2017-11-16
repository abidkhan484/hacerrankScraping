# Accepted
# Python 3

def make_array():
    num = 10**6 + 1
    ar = [0] * num

    ar[1] = 1; ar[2]=2; ar[3]=3
    for i in range(2, num//2+1):

        # this statement check for the prime numbers
        if not ar[i]:
            ar[i] = ar[i-1]+1
        else:
            ar[i] = min(ar[i-1]+1, ar[i])
        # now i just loop from 2i to i**2 and use a counter variable
        # to write down the array (memorization)
        j = 2*i; c = ar[i]+1; endLoop = i**2

        if endLoop > num:
            endLoop = num-1

        # this idea is something similar to prime sieve
        while j <= endLoop:
            
            if not ar[j]:
                ar[j] = c
            else:
                if c < ar[j]:
                    ar[j] = c
            j += i

    for i in range(num//2, num):
        if not ar[i]:
            ar[i] = ar[i-1] + 1
        else:
            ar[i] = min(ar[i], ar[i-1]+1)

    return ar

ar = make_array()

for _ in range(int(input().strip())):
    i = int(input().strip())
    print(ar[i])

