import sys


N, X = map(int, sys.stdin.readline().rstrip().split(" "))
A = list(map(int, sys.stdin.readline().rstrip().split(" ")))
answer = list()
for i in range(len(A)):
    if A[i] < X:
        answer.append(A[i])
print(" ".join([str(x) for x in answer]))