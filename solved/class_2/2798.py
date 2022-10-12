import sys
import itertools


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
value_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
combination_list = sorted([sum(x) % (M+1) for x in list(itertools.combinations(value_list, 3))], reverse=1)
print(combination_list[0])