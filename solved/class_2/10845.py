import sys
import collections


queue = collections.deque()
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    raw_commend = sys.stdin.readline().rstrip()
    if " " in list(raw_commend):
        commend, value = map(str, raw_commend.split(" "))
        if commend == "push":
            queue.append(int(value))
    else:
        commend = str(raw_commend)
        if commend == "pop":
            if len(queue) == 0:
                print("-1")
            else:
                print(queue.popleft())
        elif commend == "size":
            print(len(queue))
        elif commend == "empty":
            if len(queue) == 0:
                print("1")
            else:
                print("0")
        elif commend == "front":
            if len(queue) == 0:
                print("-1")
            else:
                print(queue[0])
        elif commend == "back":
            if len(queue) == 0:
                print("-1")
            else:
                print(queue[-1])