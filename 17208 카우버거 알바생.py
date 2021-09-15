import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
orders = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(K + 1)] for _ in range(M + 1)] for _ in range(N + 1)]

for order_cnt in range(1, len(orders)):
    cur_b, cur_f = orders[order_cnt]
    for max_burger in range(1, M + 1):
        for max_fries in range(1, K + 1):
            # 가져올 수 있으면 가져오거나 가져오지 않거나. 둘중 큰거.
            if cur_b <= max_burger and cur_f <= max_fries:
                dp[order_cnt][max_burger][max_fries] = max(
                    1 + dp[order_cnt - 1][max_burger - cur_b][max_fries - cur_f], 
                    dp[order_cnt - 1][max_burger][max_fries])
            else:
                dp[order_cnt][max_burger][max_fries] = dp[order_cnt - 1][max_burger][max_fries]

print(dp[N][M][K])



# 1등풀이. 
MIS = lambda: map(int,input().split())

n, cheese, potato = MIS()
dp = [[-999]*(potato+1) for i in range(cheese+1)]
dp[cheese][potato] = 0

for ORDER in range(n):
    c, p = MIS()
    for i in range(cheese+1-c):
        for j in range(potato+1-p):
            dp[i][j] = max(dp[i][j], dp[i+c][j+p]+1)
print(max(map(max,dp)))