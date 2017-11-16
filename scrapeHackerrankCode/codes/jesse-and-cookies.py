# Accepted
# Python 3

from heapq import *

n, m = map(int, input().split())
heap = []
for i in input().split():
    heappush(heap, int(i))

count=0
while heap[0] < m:
    if len(heap)==1:
        count = -1
        break
    a = heappop(heap)
    b = heappop(heap)
    item = a + (b<<1)
    heappush(heap, item)
    count += 1

print(count)

