# Accepted
# Python 3

from heapq import *
heap, items = [], set()
for _ in range(int(input())):
    w = list(map(int, input().split()))
    if w[0] == 1:
        heappush(heap, w[1])
        items.add(w[1])
    elif w[0] == 2:
        items.remove(w[1])
    else:
        while heap[0] not in items:
            heappop(heap)
        print(heap[0])
