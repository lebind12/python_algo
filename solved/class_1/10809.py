import sys


S = list(sys.stdin.readline().rstrip())
answer = []
for i in range(26):
    # print(chr(ord('a') + i))
    alphabet = (chr(ord('a') + i))
    if alphabet in S:
        answer.append(str(S.index(alphabet)))
    else:
        answer.append("-1")
print(" ".join(answer))