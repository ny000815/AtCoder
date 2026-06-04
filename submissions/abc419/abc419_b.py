import heapq
from heapq import heappush, heappop

Q = int(input())
heap = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        heappush(heap, q[1])
    else:
        print(heappop(heap))
