import sys


N, K = map(int, sys.stdin.readline().rstrip().split(" "))
coins = list()
coin_count = 0
for _  in range(N):
    coin = int(sys.stdin.readline().rstrip())
    coins.append(coin)
for i in reversed(range(len(coins))):
    coin = coins[i]
    if coin > K:
        continue
    if K == 0:
        break
    coin_count += K // coin
    K -= (K // coin) * coin
print(coin_count)