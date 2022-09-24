import sys


E, S, M = map(int, sys.stdin.readline().rstrip().split(" "))
year = 1
e = 1
s = 1
m = 1
while True:
    if e == E and s == S and m == M:
        print(year)
        break
    else:
        year += 1
        e += 1
        if e > 15:
            e %= 15
        s += 1
        if s > 28:
            s %= 28
        m += 1
        if m > 19:
            m %= 19