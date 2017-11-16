# Accepted
# Python 3

m, n = input().split()
m, n = int(m), int(n)

li = list(map(int, input().split()))
pri = int(input().strip())

li[n] = 0
su = 0
for i in li:
    su += i

su = su//2
if su == pri:
    print('Bon Appetit')
else:
    print(pri-su)

