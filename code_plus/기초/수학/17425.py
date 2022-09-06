import sys
import math
"""
def get_gvalue(num : int):
    sum = 0
    for i in range(1, num + 1):
        sum += i * (num // i)
    return sum


"""

"""
약수의 합 2와 같은 방식이지만 이때는 테스트의 개수가 정해져있음
테스트케이스 100,000개를 하나의 프로그램에서 실행할 수 있도록 구현해야함 
약수의 합을 구했을 때 이미 구한건 다시 구하지 않아야 함.
그래서 g(num) 값을 저장하는 배열을 선언.
g(num) = g(num-1) + f(num)
""" 

"""
def get_fvalue(num : int):
    divisor_values = []
    divisor_appos = []
    # 약수는 제곱근 + 1 까지만
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisor_values.append(i)

    for divisor in divisor_values:
        divisor_appos.append(num // divisor)
    return sum(list(set(divisor_values + divisor_appos)))

def get_gvalue(num : int):
    global f_values
    sum = 0
    if g_values[num] != 0:
        return g_values[num]
    for value in range(num):
        # 이미 구했으면
        if f_values[value] != 0:
            sum += f_values[value]
        # 아직 안구했으면
        else:
            f_values[value] = get_fvalue(value)
            sum += f_values[value]
    g_values[num] = sum + get_fvalue(num)
    return g_values[num]

N = int(sys.stdin.readline())
f_values = [0] * 1000001
g_values = [0] * 1000001
for _ in range(N):
    num = int(sys.stdin.readline())
        # 아직 안구했으면 구한다.
    print(get_gvalue(num))
"""

"""
위의 식으로는 1,000,000 값의 약수를 구하는 것 부터 시간초과가 뜬다.
에라토스테네스의 체를 이용하여 dp 테이블을 bottom-up하는 방식으로 구현한다.
2의 배수인 N의 f(N) 값은 모두 2 이상이다. (약수에 2가 있으니까)
따라서 최대값 1,000,000 까지 dp 테이블을 채우고 해당 값의 합을 구하면 된다. 
"""

MAX = 1000001
N = int(sys.stdin.readline())
f_values = [1] * MAX
g_values = [0] * MAX
for i in range(2, MAX):
    j = 1
    try:
        while i * j < MAX:
            f_values[i * j] += i
            j += 1
    except IndexError:
        print(i * j)

for i in range(1, MAX):
    g_values[i] = g_values[i-1] + f_values[i]

for _ in range(N):
    num = int(sys.stdin.readline())
    print(g_values[num])