import sys


found_one = list(map(int, sys.stdin.readline().split(" ")))
goal = [1, 1, 2, 2, 2, 8]
answer = list()
for i in range(len(found_one)):
    answer.append(str(goal[i] - found_one[i]))

str = " ".join(answer)
print(str)