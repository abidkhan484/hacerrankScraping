# Wrong Answer
# Python 3

def make_array():
    num = 10**6 + 1
    ar = [0] * num

    for i in range(2, 1001):
        j = i*i; c = i
        while j < num:
            ar[j] = c
            c += 1
            j += i
    
    for i in range(num):
        if ar[i]==0:
            ar[i] = i-1
    
    return ar


def down_to_zero(i, count=0):
    # bcoz the array is not 0 indexed
    if ar[i]==-1:
        return count
    return down_to_zero(ar[i], count+1)

ar = make_array()
for _ in range(int(input().strip())):
    print(down_to_zero(int(input().strip())))

