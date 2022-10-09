import sys


N = str(sys.stdin.readline().rstrip())
num_list = [int(x) for x in list(N)]

# 30의 배수인 지 확인
if sum(num_list) % 3 == 0 and num_list.count(0) >= 1:
    print("".join([str(x) for x in sorted(num_list, reverse=1)]))
else:
    print(-1)