import sys
import itertools


N = int(sys.stdin.readline().rstrip())
perm_line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
perm_list = list(itertools.permutations(range(1, N+1), N))

# print(perm_list.index(tuple(perm_line)))
idx = perm_list.index(tuple(perm_line))
if (idx == len(perm_list) - 1):
    print(-1)
else:
    print(" ".join([str(x) for x in perm_list[idx + 1]]))