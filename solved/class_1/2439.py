import sys


N = int(sys.stdin.readline().rstrip())
for i in range(1, N+1):
    string_a = ' ' * (N - i)
    string_b = '*' * i
    print(string_a + string_b)