import sys


N = int(sys.stdin.readline().rstrip())
number_list = []
for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    number_list.append(number)
number_list = sorted(number_list)
for idx in range(N):
    print(number_list[idx])