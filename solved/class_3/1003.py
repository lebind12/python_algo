import sys

zero_count_list = [-1] * 41
one_count_list = [-1] * 41
zero_count_list[0] = one_count_list[0] = 0
zero_count_list[1] = one_count_list[1] = 1

def fibonacci(order):
    global fibonacci_list
    global zero_count_list
    global one_count_list

    if order == 1:
        one_count += 1
        return 1
    elif order == 0:
        zero_count += 1
        return 0
    return fibonacci(order - 1) + fibonacci(order - 2)
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    zero_count = 0
    one_count = 0
    N = int(sys.stdin.readline().rstrip())
    fibonacci(N)
    print(str(zero_count) + " " + str(one_count))