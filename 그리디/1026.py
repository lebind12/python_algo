import sys


N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split(" ")))
B = list(map(int, sys.stdin.readline().rstrip().split(" ")))
sum = 0
for _ in range(N):
    maximum_A = max(A)
    minimum_B = min(B)
    sum += maximum_A * minimum_B
    A.remove(maximum_A)
    B.remove(minimum_B)
print(sum)