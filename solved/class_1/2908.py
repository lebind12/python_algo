import sys


A, B = map(int, sys.stdin.readline().rstrip().split(" "))
string_A = (reversed(list(str(A))))
string_B = (reversed(list(str(B))))
num_A = int("".join(list(string_A)))
num_B = int("".join(list(string_B)))
if num_A >= num_B:
    print(str(num_A))
else:
    print(str(num_B))