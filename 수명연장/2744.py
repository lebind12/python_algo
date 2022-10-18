import sys


S = list(sys.stdin.readline().rstrip())
for i in range(len(S)):
    if ord(S[i]) >= ord('a') and ord(S[i]) <= ord('z'):
        S[i] = S[i].upper()
    elif ord(S[i]) >= ord('A') and ord(S[i]) <= ord('Z'):
        S[i] = S[i].lower()
print("".join(S))