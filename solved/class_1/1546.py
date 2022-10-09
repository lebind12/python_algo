from audioop import avg
import sys


N = int(sys.stdin.readline().rstrip())
score_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
M = max(score_list)
score_list = [x / M * 100 for x in score_list]
print(sum(score_list) / len(score_list))