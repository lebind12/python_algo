import sys
import itertools


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
perm_list = list(itertools.product(range(1, N+1), repeat=M))
for item in perm_list:
    print(" ".join([str(x) for x in item]))