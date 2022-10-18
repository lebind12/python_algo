import sys


A, B = map(int, sys.stdin.readline().rstrip().split(" "))
count = 1
while True:
    if B < A:
        print("-1")
        break
    elif A == B:
        print(count)
        break
    else:
        if B % 2 == 1:
            B = B // 10
        else:
            B /= 2
        count += 1
