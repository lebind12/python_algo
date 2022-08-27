from collections import deque


def solve():
    N = int(input())    
    
    # 3킬로 봉지 5킬로 봉지
    dp = dict()
    queue = deque()
    value = int()
    # dp[3] = 1, dp[5] = 1
    dp[3] = 1
    dp[5] = 1
    queue.append(3)
    queue.append(5)

    # dp[6] = dp[3] + 1
    # dp[8] = dp[5] + 1
    # dp[10] = dp[5] + 1

    # dp[9] = dp[6] + 1
    # dp[11] = dp[8] + 1
    # dp[13] = dp[8] + 1
    # dp[15] = dp[10] + 1
    while True:
        value = queue.popleft()
        if (value == N):
            print(dp[value])
            return
        # 언제 멈춰야하는가?
        # 3, 5 생각해보면 6, 8, 10 들어가니까
        # 9 11, 15 이므로 다음 타임 생각해보면 내가 9 구하려고 했는데 16부터는 전혀 상관없으니까
        if (value > N + 6):
            break
        if value + 3 not in dp.keys():
            dp[value + 3] = dp[value] + 1
            queue.append(value + 3)
        if value + 5 not in dp.keys():
            dp[value + 5] = dp[value] + 1
            queue.append(value + 5)

    print("-1")

if __name__ == "__main__":
    solve()