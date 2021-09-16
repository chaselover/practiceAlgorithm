import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    coins = {}
    target = 0
    for _ in range(N):
        a, b = map(int, input().split())
        coins[a] = b
        target += a*b
    if target&1:
        print(0)
        continue
    target //= 2
    dp = [1] + [0] * (target)
    for coin in coins:
        for money in range(target,coin-1,-1):
            if dp[money-coin]:
                for j in range(coins[coin]):
                    if money + coin*j <= target:
                        dp[money + coin*j] = 1
    print(dp[target])