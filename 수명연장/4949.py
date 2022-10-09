import sys


leftbrace_list = []
while True:
    string = sys.stdin.readline().rstrip()
    if string == ".":
        break
    for i in range(len(string)):
