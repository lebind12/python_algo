import sys
import math


def get_divisor(num : int):
    divisor_list = []
    divisor_appo = []
    # print(int(round(math.sqrt(num), 0) + 1))
    for i in range(1, int(round(math.sqrt(num), 0) + 1)):
        # print(i)
        if num % i == 0:
            divisor_list.append(i)
    for value in divisor_list:
        divisor_appo.append(num // value)
        
    return list(set(divisor_list + divisor_appo))

def get_fvalue(num : int):
    return sum(get_divisor(num))

def get_gvalue(num : int):
    sum = 0
    for value in range(1, num + 1):
        sum += get_fvalue(value)
    return sum

print(get_gvalue(1000000))