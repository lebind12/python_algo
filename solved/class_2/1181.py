import sys


N = int(sys.stdin.readline().rstrip())
words = list()
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    words.append(word)
words = sorted(list(set(words)))
words = sorted(words, key=len)
for i in range(len(words)):
    print(words[i])