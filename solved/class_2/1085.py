import sys


x, y, w, h = map(int, sys.stdin.readline().rstrip().split(" "))
values = [x, y, w - x, h - y]
print(min(values))