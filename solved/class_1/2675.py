import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    R, S = map(str, sys.stdin.readline().rstrip().split(" "))
    R = int(R)
    answer_string = ""
    for i in range(len(S)):
        answer_string += S[i] * R
    print(answer_string)