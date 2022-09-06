import sys
import math

"""
- 직관적인 알고리즘
- 시간초과에 걸림
- math에 익숙해질 수 있었음.

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
"""

"""
입력값 num에 대하여
g(num)을 계산할 때 f(1) 부터 f(num)까지 계산하면서
2의 배수는 약수로 2를 항상 갖고, 3의 배수는 약수로 항상 3을 갖기 때문에
g(num)을 계산할 때 2가 1부터 num까지의 수 중 2의 배수만큼 존재하게 됨.
이를 이용하여 문제를 풀이
"""

def get_gvalue(num : int):
    sum = 0 # 합을 저장할 변수
    for i in range(1, num + 1):
        sum += i * (num // i) # i는 num 에서 i를 나눈 몫만큼 존재
    return (sum)

num = int(sys.stdin.readline())
print(get_gvalue(num))