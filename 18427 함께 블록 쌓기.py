import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N) ]
dp = [0]*(H+1)

for box in boxes:
    for idx in range(H,0,-1):
        if not dp[idx]: continue
        for num in box:
            if idx + num > H: continue
            dp[idx+num] += dp[idx]
    for num in box:
        dp[num] += 1
print(dp[H]%10007)