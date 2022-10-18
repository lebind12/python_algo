import sys


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
data = dict()
for _ in range(N):
    url, password = sys.stdin.readline().rstrip().split(" ")
    data[url] = password
for _ in range(M):
    url = sys.stdin.readline().rstrip()
    print(data[url])