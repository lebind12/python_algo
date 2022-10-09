import sys


num = [int(x) for x in list(str(sys.stdin.readline().rstrip()))]
print("".join([str(x) for x in list(sorted(num, reverse=1))]))