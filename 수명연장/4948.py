import sys
import collections


p_list = [1] * 250000
# 123,456이 쪼끄마하니까 소수인걸 먼저 찾아야겠다.
# p_list 가 1이면 소수
p_list[0] = 0
p_list[1] = 0
for idx in range(2, len(p_list)):
    step = 2
    if p_list[idx] == 1:
        while True:
            if idx * step >= len(p_list):
                break
            p_list[idx * step] = 0
            step += 1

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    # 자연수 n이 주어졌을 때 n보다 크고 2n보다 작거나 같은 소수의 개수
    # 1 <= n <= 123,456
    counter = collections.Counter(p_list[n + 1 : 2 * n + 1])
    print(counter.get(1))