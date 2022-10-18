import sys
from collections import deque


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
graph = [[] for _ in range(N + 1)]
bacon = [0] * (N + 1)
bacon[0] = 999999
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[A].append(B)
    graph[B].append(A)

for i in range(1, N+1):
    visited = [0] * (N + 1)
    visited[0] = -1
    queue = deque()
    queue.append((i, 1))
    # bfs
    while True:
        if len(queue) == 0:
            break
        v, count = queue.popleft()
        if visited[v] == 1:
            continue
        else:
            visited[v] = count
            for vertex in graph[v]:
                if visited[v] == 0:
                    queue.append((v, count + 1))
print(bacon)
