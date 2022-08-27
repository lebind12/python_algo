import math


def solve():
    A, B, V = map(int, input().split(' '))

    # V-A 이상으로만 도달하면 그날 다오름
    goal = V - A
    # 나눈 값을 올림처리
    print(math.ceil(goal / (A-B)) + 1)

if __name__ == "__main__":
    solve()