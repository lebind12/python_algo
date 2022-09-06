import sys
import math


def is_prime(num : int):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

while True:
    value = int(sys.stdin.readline())
    founded = False
    if value == 0:
        break
    for i in range(1, value // 2 + 1, 2):
        if is_prime(i) and is_prime(value - i):
            print(str(value) + " = " + str(i) + " + " + str(value - i))
            founded = True
            break
    if founded == False:
        print("Goldbach's conjecture is wrong.")
# for value in range(6, 1000000, 2):
#     founded = False
#     if value == 0:
#         break
#     for i in range(1, value // 2, 2):
#         if is_prime(i) and is_prime(value - i):
#             print(str(value) + " = " + str(i) + " + " + str(value - i))
#             founded = True
#             break
#     if founded == False:
#         print("Goldbach's conjecture is wrong.")