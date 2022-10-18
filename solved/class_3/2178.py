import sys
from collections import deque


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
board = list()
for _ in range(N):
    line = list(sys.stdin.readline().rstrip())
    board.append(line)

queue = deque()
queue.append((0, 0, 1))
board[0][0] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while True:
    if len(queue) == 0:
        break
    x, y, count = queue.popleft()
    x = int(x)
    y = int(y)
    if x == N - 1 and y == M - 1:
        print(count)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if board[nx][ny] == "1":
                queue.append((nx, ny, count + 1))
                board[nx][ny] = "0"

