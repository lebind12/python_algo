import sys
import math


N = int(sys.stdin.readline().rstrip())
value = list(str(math.factorial(N)))
zero_counter = 0
for i in reversed(range(len(value))):
    if value[i] == '0':
        zero_counter += 1
    else:
        break
print(zero_counter)