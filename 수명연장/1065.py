import sys


N_INF = -999
N = int(sys.stdin.readline().rstrip())
count = 0
for value in range(1, N+1):
    value = [int(x) for x in list(str(value))]
    gap = N_INF
    if len(value) == 1:
        count += 1
        continue
    for idx in range(1, len(value)):
        if gap == N_INF:
            gap = value[idx] - value[idx - 1]
        if value[idx] - value[idx - 1] != gap:
            break
        else:
            if idx == len(value) - 1:
                count += 1
print(count)