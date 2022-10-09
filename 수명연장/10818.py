import sys


N = int(sys.stdin.readline().rstrip())
values = list(map(int, sys.stdin.readline().rstrip().split(" ")))
answer = list()
answer.append(min(values))
answer.append(max(values))
print(" ".join(str(x) for x in answer))