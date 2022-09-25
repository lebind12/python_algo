import sys


# 1초의 1억번을 기준으로 하자
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
no_buttons = list()
min_diff = abs(N - 100)
if M != 0:
    no_buttons = list(map(int, sys.stdin.readline().split(" ")))

def is_broken(channel):
    global no_buttons
    str_channel = str(channel)
    for i in range(len(str_channel)):
        if int(str_channel[i]) in no_buttons:
            return -1
    return 1

# N이 50만까지니까 비교적 적음
for channel in range(1000001):
    if is_broken(channel) == -1:
        continue
    else:
        diff = abs(N - channel) + len(str(channel))
        if min_diff > diff:
            min_diff = diff

print(min_diff)