import sys
import itertools


N, M = map(int, sys.stdin.readline().split(" "))
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
answer = list(itertools.permutations(range(1, N+1), M))
answer_list = []

for item in answer:
    item = list(item)
    item = sorted(item)
    if item not in answer_list:
        answer_list.append(item)

for item in answer_list:
    print(" ".join([str(x) for x in item]))