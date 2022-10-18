import sys


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
never_heard = set()
never_seen = set()
for _ in range(N):
    value = sys.stdin.readline().rstrip()
    never_heard.add(value)
for _ in range(M):
    value = sys.stdin.readline().rstrip()
    never_seen.add(value)
intersection_set = sorted(list(never_heard.intersection(never_seen)))
print(len(intersection_set))
for i in range(len(intersection_set)):
    print(intersection_set[i])