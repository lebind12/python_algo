import sys


N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

# 인접한 행렬을 검색
# 하나의 원소에 대해 우하향으로 인접한 색이다른 사탕을 검색
# 바꿔보고 영향이 가는 행/열을 검사하여 연속 값이 가장 큰 경우를 확인 및 저장

dx = [1, 0]
dy = [0, 1]
max_seq = -1

def check_max_seq(list):
    count = 1
    max_count = 0
    for i in range(0, len(list) - 1):
        if list[i] == list[i + 1]:
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 1
    return count

def count_seq(board, x, y, nx, ny):
    max_seq = -1
    # 가로 교체
    if y == ny:
        # 가로 교체는 y열, ny열, x행 검사
        test_line = [y, ny, x]
        for line in test_line:
            # 가로 검사
            if line == x:
                    count = check_max_seq(board[line])
                    if max_seq < count:
                        max_seq = count
            # 세로 검사
            else:
                for i in range(N):
                    board[i][line]
    # 세로 교체
    else:
        # 세로 교체는 y열, x행, nx행 검사
        test_line = [y, x, nx]
        for line in test_line:
            # 세로 검사
            if line == y:
                for i in range(N):
                    board[i][line]
            # 가로 검사
            else:
                for i in range(N):
                    board[line][i]



# 근데 2차원 행렬 순회 코드가 바로 떠오르지 않음 => 연습해야겠당
for x in range(N):
    for y in range(N):
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            # nx가 N을 넘기면 행렬 밖임
            if nx < N and ny < N:
                # 인접 사탕 색이 다르면
                if board[x][y] != board[nx][ny]:
                    # board의 카피본을 따서
                    copied_board = board.copy()
                    # 둘이 바꿔봄
                    copied_board[x][y], copied_board[nx][ny] = copied_board[nx][ny], copied_board[x][y]
                    # 연관된 행/열 의 연속을 계산함
                    count_seq(copied_board, x, y, nx, ny)
