import sys
import math


K, L = map(int, sys.stdin.readline().rstrip().split(" "))
found = 0

for div in range(2, L):
    if K % div == 0:
        found = 1
        print("BAD " + str(div))
        break

if found == 0:
    print("GOOD")