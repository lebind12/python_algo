import sys


N = int(sys.stdin.readline().rstrip())
string_len = 0
digit = 10
# digit을 기준으로 digit보다 작으면 (N - digit/10 + 1) * len(str(digit))을 더함.
# digit보다 크면 (digit - 1) * len(str(digit/10)) 을 더함

def solve():
    global N
    global digit
    global string_len
    if N < 10:
        print(N * 1)
        return
    while True:
        if digit <= N:
            string_len += len(str(digit - 1)) * int(digit * 0.9)
            digit *= 10
        else:
            string_len += len(str(digit - 1)) * (N - int(digit/10) + 1)
            break
    print(string_len)
solve()