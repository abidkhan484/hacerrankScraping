# Runtime Error
# Python 3

# this problem is not solved yet
from heapq import *

n, m = map(int, input().split())
heap = []
for i in input().split():
    heappush(heap, int(i))

count=0
while heap[0] < m:
    a = heappop(heap)
    b = heappop(heap)
    item = a + (b<<1)
    heappush(heap, item)
    count += 1

print(count) if count else print(-1)

