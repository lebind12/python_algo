import sys
from collections import deque


board = list()
queue = deque()
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split(" "))
    board = [[0] * M for _ in range(N)]
    count = 0

    # making board
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split(" "))
        board[Y][X] = 1

    # searching 1
    for i in range(N):
        for j in range(M):
            # print(str(i) + " " + str(j))
            if board[i][j] == 1:
                queue.append((i, j))
                board[i][j] = 0
                while True:
                    if len(queue) == 0:
                        break
                    value = queue.popleft()
                    x, y = value
                    dx = [-1, 1, 0, 0]
                    dy = [0, 0, -1, 1]

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[x]):
                            if board[nx][ny] == 1:
                                queue.append((nx, ny))
                                board[nx][ny] = 0
                count += 1
    print(count)