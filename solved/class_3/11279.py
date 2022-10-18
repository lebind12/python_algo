import sys
import heapq


N = int(sys.stdin.readline().rstrip())
heap = list()
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(int(heapq.heappop(heap)) * -1)
    else:
        heapq.heappush(heap, x * -1)