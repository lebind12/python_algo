import sys
import collections


deque = collections.deque()
N = int(sys.stdin.readline().rstrip())
for _  in range(N):
    raw_commend = sys.stdin.readline().rstrip()
    if " " in raw_commend:
        commend, value = raw_commend.split(" ")
        if commend == "push_front":
            deque.appendleft(int(value))
        elif commend == "push_back":
            deque.append(int(value))
    else:
        commend = raw_commend
        if commend == "pop_front":
            if len(deque) == 0:
                print("-1")
            else:
                print(deque.popleft())
        elif commend == "pop_back":
            if len(deque) == 0:
                print("-1")
            else:
                print(deque.pop())
        elif commend == "size":
            print(len(deque))
        elif commend == "empty":
            if len(deque) == 0:
                print("1")
            else:
                print("0")
        elif commend == "front":
            if len(deque) == 0:
                print("-1")
            else:
                print(deque[0])
        elif commend == "back":
            if len(deque) == 0:
                print("-1")
            else:
                print(deque[-1])