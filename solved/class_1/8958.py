import sys


N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    case = list(str(sys.stdin.readline().rstrip()))
    combo = 0
    point = 0
    for idx in range(len(case)):
        if case[idx] == 'O':
            combo += 1
            point += combo
        else:
            combo = 0
    print(point)