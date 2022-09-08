import sys


sys.setrecursionlimit(100000)
heights = []
founded = False
for _ in range(9):
    heights.append(int(sys.stdin.readline()))

def recursion(chosen:list, start):
    # print(chosen)
    global founded
    if founded == True:
        return
    if len(chosen) == 7:
        if sum(chosen) == 100:
            chosen.sort()
            for i in range(7):
                print(chosen[i])
            founded = True
            return
    if len(chosen) > 7:
        return

    choosed = chosen.copy()
    for i in range(start, len(heights)):
        choosed.append(heights[i])
        recursion(choosed, i + 1)
        choosed.pop()

recursion([], 0)