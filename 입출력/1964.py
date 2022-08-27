def solve():
    N = int(input())
    dp = list()
    # dp[0] = -1
    dp.append(-1)
    # dp[1] = 5
    dp.append(5)

    # dp[2] = dp[1] + 3 + 3 + 3 - 2
    # dp[3] = dp[2] + 4 + 4 + 4 - 2
    # dp[n] = dp[n-1] + 3*(n+1) - 2

    for i in range(2, N + 1):
        value = dp[i-1] + (3 * (i + 1) - 2)
        dp.append(value)
    print(dp[N] % 45678)

if __name__ == "__main__":
    solve()