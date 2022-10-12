import sys


INF = 99999999
N = int(sys.stdin.readline().rstrip())
string = list(str(N))
start = N - len(string) * 10
if start < 0:
    start = 0
answer = INF
for i in range(start, N + 1):
    string_value = [int(x) for x in list(str(i))]
    sum_value = sum(string_value)
    dist_value = i + sum_value
    if N == dist_value:
        answer = i
        break
if answer == INF:
    print("0")
else:
    print(answer)