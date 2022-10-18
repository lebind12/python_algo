import sys

def solve():
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        print(0)
        return
    elif n == 1 or n == 2:
        print(1)
        return
    A = 0
    B = 1
    C = -1
    for _ in range(2, n+1):
        C = A + B
        A, B = B, C
    print(C)
solve()