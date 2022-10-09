import sys


N = int(sys.stdin.readline().rstrip())
values = [int(x) for x in list(str(sys.stdin.readline().rstrip()))]
print(sum(values))