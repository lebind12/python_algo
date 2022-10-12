import sys
import math

a, b = map(int, sys.stdin.readline().rstrip().split(" "))
gcd = math.gcd(a, b)

print(str(gcd) + "\n" + str(a * b // gcd))