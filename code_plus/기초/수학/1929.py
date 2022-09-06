import sys
import math


def is_prime(num : int):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

M, N = map(int, sys.stdin.readline().rstrip().split(" "))
for value in range(M, N+1):
    if value == 1:
        continue
    if is_prime(value):
        print(value)