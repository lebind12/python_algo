import sys


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
values = list(map(int, sys.stdin.readline().rstrip().split(" ")))
sum_values = list()
sum_values.append(0)
for i in range(N):
    sum_values.append(sum_values[i] + values[i])
for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split(" "))
    print(sum_values[j] - sum_values[i-1])