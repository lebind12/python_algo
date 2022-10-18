import sys
from collections import deque
from pprint import pprint


M, N = map(int, sys.stdin.readline().rstrip().split(" "))
board = []
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    board.append(line)

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            queue.append((i, j, 0))

# bfs start
while True:
    if len(queue) == 0:
        break
    x, y, count = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if board[nx][ny] == 0:
                board[nx][ny] = count + 1
                queue.append((nx, ny, count + 1))

# 2차원에 0이 있으면 -1 아니면 count
if all(0 not in l for l in board):
    print(count)
else:
    print(-1)