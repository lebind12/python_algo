import sys
import collections


N = int(sys.stdin.readline().rstrip())
values = list(map(int, sys.stdin.readline().rstrip().split(" ")))
counter = collections.Counter(values)
v = int(sys.stdin.readline().rstrip())
count = counter.get(v)
if count == None:
    print("0")
else:
    print(counter.get(v))