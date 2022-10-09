import sys
import collections


word = str(sys.stdin.readline().rstrip()).upper()
counter = collections.Counter(word)
common_list = counter.most_common()
if len(common_list) > 1 and common_list[0][1] == common_list[1][1]:
    print('?')
else:
    print(common_list[0][0])