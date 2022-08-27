from collections import deque


def solve():
    N, M = map(int, input().split(" "))
    count = 0 # 쪼개는 횟수
    # 쪼개는 횟수의 최소
    # 큐를 써서 풀이
    # 맨처음 입력받은거 큐에 넣으면 그거 쪼개서 큐에 넣음
    # 쪼개는건 가로 세로 중에 큰거
    c = [N, M]
    d = deque()
    d.append(c)

    # 쪼개기
    while True:
        if len(d) == 0:
            break
        # 큐에 있는거 꺼냄
        c = d.pop()
        # [1, 1] 초콜렛이면 아무것도 안함 
        if c[0] == 1 and c[1] == 1:
            continue
        # 가로 세로 중 큰 쪽으로 쪼개고 다시 큐로 넣음
        if c[0] > c[1]:
            piece1 = [c[0]//2, c[1]]
            piece2 = [c[0] - c[0]//2, c[1]]
            d.append(piece1)
            d.append(piece2)
            count = count + 1
        else:
            piece1 = [c[0], c[1]//2]
            piece2 = [c[0], c[1] - c[1]//2]
            d.append(piece1)
            d.append(piece2)
            count = count + 1
    print(count)


if __name__ == "__main__":
    solve()