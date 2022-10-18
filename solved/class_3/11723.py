import sys


value_list = list()
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    raw_commend = sys.stdin.readline().rstrip()
    if ' ' in raw_commend:
        commend, value = raw_commend.split(" ")
        value = int(value)
        if commend == "add":
            if value not in value_list:
                value_list.append(value)
        elif commend == "remove":
            if value in value_list:
                value_list.remove(value)
        elif commend == "check":
            if value in value_list:
                print("1")
            else:
                print("0")
        elif commend == "toggle":
            if value in value_list:
                value_list.remove(value)
            else:
                value_list.append(value)
    else:
        commend = raw_commend
        if commend == "all":
            value_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        elif commend == "empty":
            value_list = []

# 비트마스크를 이용하여 풀어야함
# 왜냐하면 메모리 제한이 4MB니까.