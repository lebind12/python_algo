import sys


def charge_set(piece_list):
    for i in range(10):
        piece_list[i] += 1

N = list(str(sys.stdin.readline().rstrip()))
piece_list = [0] * 10
for idx in range(len(N)):
    number = int(N[idx])
    # print(number)
    if number == 6:
        if piece_list[number] == 0:
            if piece_list[9] != 0:
                piece_list[9] -= 1
            else:
                charge_set(piece_list)
                piece_list[number] -= 1
        else:
            piece_list[number] -= 1
    elif number == 9:
        if piece_list[number] == 0:
            if piece_list[6] != 0:
                piece_list[6] -= 1
            else:
                charge_set(piece_list)
                piece_list[number] -= 1
        else:
            piece_list[number] -= 1
    else:
        if piece_list[number] == 0:
            charge_set(piece_list)
            piece_list[number] -= 1
        else:
            piece_list[number] -= 1
    # print(piece_list)
print(max(piece_list))
# print(piece_list)