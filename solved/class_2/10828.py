import sys
import collections


stack = collections.deque()
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    raw_commend = sys.stdin.readline().rstrip()
    if " " in list(raw_commend):
        commend, value = map(str, raw_commend.split(" "))
        if commend == "push":
            stack.append(int(value))
    else:
        commend = str(raw_commend)
        if commend == "pop":
            if len(stack) == 0:
                print("-1")
            else:
                print(stack.pop())
        elif commend == "size":
            print(len(stack))
        elif commend == "empty":
            if len(stack) == 0:
                print("1")
            else:
                print("0")
        elif commend == "top":
            if len(stack) == 0:
                print("-1")
            else:
                print(str(stack[len(stack) - 1]))