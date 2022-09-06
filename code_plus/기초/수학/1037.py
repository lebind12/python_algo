import sys


n = int(sys.stdin.readline())
divisions = list(map(int, sys.stdin.readline().rstrip().split(" ")))
print(max(divisions) * min(divisions))