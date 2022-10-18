import sys


T = int(sys.stdin.readline().rstrip())
# 1, 1, 1, 2, 2 까지는 상수.
# 3 = 1 + 2, 4 = 1 + 3, 5 = 1 + 4
# 7 = 2 + 5
# A[i] (i > 4) = A[i - 5] + A[i - 1]
# N은 1에서 100까지니까 미리 만들어두자.
padoban = [1, 1, 1, 2, 2]
for i in range(5, 101):
    padoban.append(padoban[i - 5] + padoban[i - 1])
for _  in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(padoban[N - 1])
