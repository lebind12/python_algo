import sys


N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

print(board)