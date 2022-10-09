import sys


price = 1000 - int(sys.stdin.readline().rstrip())
# 500, 100, 50, 10, 5, 1
# 탐욕법으로 문제를 해결
# 출력은 잔돈의 개수
coins = [500, 100, 50, 10, 5, 1]
coin_count = 0
for coin in coins:
    if coin <= price:
        coin_count += price // coin
        price -= (price // coin) * coin
print(coin_count)