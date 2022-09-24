import sys
import itertools


N, M = map(int, sys.stdin.readline().split(" "))
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
answer = list(itertools.permutations(range(1, N+1), M))

for item in answer:
    string = ""
    for idx in range(len(item)):
        if idx == len(item) - 1:
            string += str(item[idx])
        else:
            string += str(item[idx]) + " "
    print(string)