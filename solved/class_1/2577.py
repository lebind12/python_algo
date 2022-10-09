import collections
import sys


A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
value = [int(x) for x in list(str(A * B * C))]
counter = collections.Counter(value)
# print(counter)
for i in range(10):
    if i not in counter.keys():
        print("0")
    else:
        print(counter.get(i))