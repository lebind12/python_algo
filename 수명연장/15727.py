import sys


L = int(sys.stdin.readline().rstrip())
t = L // 5
r = L % 5
if r > 0:
    t += 1
print(t)