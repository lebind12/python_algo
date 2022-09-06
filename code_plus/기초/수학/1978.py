import sys
import math


"""
N <= 100
num <= 1000
"""
def is_prime(num : int):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False

    return True

N = int(sys.stdin.readline())
values = map(int, sys.stdin.readline().rstrip().split(" "))
count = 0
for i in values:
    if i == 1:
        continue
    if is_prime(i):
        count += 1
print(count)