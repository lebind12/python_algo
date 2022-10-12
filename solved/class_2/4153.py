import sys
import math


while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))
    values = [a, b, c]
    if a == 0 and b == 0 and c == 0:
        break
    l = max(values)
    s = min(values)
    for i in range(3):
        if values[i] != l and values[i] != s:
            m = values[i]
    if s * s + m * m == l * l:
        print("right")
    else:
        print("wrong")