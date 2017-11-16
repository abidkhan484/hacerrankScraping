# Wrong Answer
# Python 3

from math import sqrt

def prime_list(num):

    li = [0]*(num+1); li[0]=1; li[1]=1; sqr = int(sqrt(num+1))
    for i in range(4, num+1, 2):
        li[i] = 1

    for i in range(3, sqr, 2):
        tmp = i+i
        if not li[tmp]:
            while tmp < num+1:
                li[tmp] = 1
                tmp += i

    prime = []
    for i in range(num+1):
        if not li[i]:
            prime.append(i)

    return prime


def check_prime(num):

    if (not (num&1) and num!=2) or (num==1):
        print('Not prime')
        return

    prime = prime_list(int(sqrt(num)+1))
    for i in range(len(prime)):
        if not (num%prime[i]):
            print('Not prime')
            return
    else:
        print('Prime')
    

for _ in range(int(input().strip())):
    check_prime(int(input().strip()))

