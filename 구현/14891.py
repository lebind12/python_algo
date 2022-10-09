import sys


def turn_clock(chain):
    temp_chain = chain.copy()
    # 시계방향으로 회전하는 함수
    for i in range(8):
        chain[(i + 1) % 8] = temp_chain[i]
    return chain

def turn_unclock(chain):
    temp_chain = chain.copy()
    # 시계방향으로 회전하는 함수
    for i in range(8):
        chain[i - 1] = temp_chain[i]
    return chain

chains = [[] for _ in range(4)]
for i in range(4):
    chain = list(map(int, sys.stdin.readline().rstrip()))
    chains[i] = chain

K = int(sys.stdin.readline().rstrip())
for _ in range(K):
    index, direction = map(int, sys.stdin.readline().rstrip().split(" "))
    # chains[idx][0]은 12시 방향. 그 다음으로 시계방향으로 극을 의미함
    # N극은 0, S극은 1로 표시.
    # chains[n][2]와 chains[n+1][-2]가 맞닿아있음
    # 맞닿은 극이 같은 극이면 회전하지 않음
    # 다른 극이면 n+1의 톱니가 n의 회전방향과 다른방향으로 같이 돔
    # 회전하면 chains[n]의 원소를 한 칸씩 밀어야함.
    