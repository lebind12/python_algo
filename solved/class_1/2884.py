import sys


H, M = map(int, sys.stdin.readline().rstrip().split(" "))
if M < 45:
    M += 60
    M -= 45
    H -= 1
else:
    M -= 45
if H < 0:
    H += 24
print(" ".join([str(H), str(M)]))
