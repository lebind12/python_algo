import sys


N = int(sys.stdin.readline().rstrip())
count = 0
for _ in range(N):
    alpha_list = []
    word = list(str(sys.stdin.readline().rstrip()))
    wrong_flag = 0
    for idx in range(len(word)):
        if word[idx] in alpha_list:
            if word[idx] != word[idx - 1]:
                wrong_flag = 1
                break
        else:
            alpha_list.append(word[idx])
    if wrong_flag == 0:
        count += 1
print(count)