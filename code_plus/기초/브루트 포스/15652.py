import sys
import itertools


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
perm_list = list(itertools.product(range(1, N+1), repeat=M))
for idx in range(len(perm_list)):
    perm_list[idx] = sorted(perm_list[idx])