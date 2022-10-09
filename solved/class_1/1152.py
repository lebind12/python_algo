import sys


string = list(sys.stdin.readline().rstrip().strip(" ").split(" "))
if '' in string:
    string.remove('')
print(len(string))