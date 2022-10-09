import sys


sound_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
if sound_list == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif sound_list == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
else:
    print("mixed")