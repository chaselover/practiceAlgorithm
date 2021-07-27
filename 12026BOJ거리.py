import sys
input = sys.stdin.readline

N = int(input())
BOJ_avenue = input().rstrip()
# 스타트 i i+1부터N번까지 점프 가능 K만큼 점프하는 에너지 k*k
# 가장 가까운 BOJ를 순서대로 밟기.
# 누적 -> dp(전 상태에 따라 변화값이 존재하는 조건.)
dp = [float('inf')]*N
dp[0] = 0
for i in range(1,N):
    for j in range(i):
        if BOJ_avenue[j]=='B' and BOJ_avenue[i]=='O':
            dp[i] = min(dp[i],dp[j]+ pow(i-j,2))
        elif BOJ_avenue[j]=='O' and BOJ_avenue[i]=="J":
            dp[i] = min(dp[i],dp[j]+ pow(i-j,2))
        elif BOJ_avenue[j]=='J' and BOJ_avenue[i]=='B':
            dp[i] = min(dp[i],dp[j]+ pow(i-j,2))

if dp[N-1] != float('inf'):
    print(dp[N-1])
else:
    print(-1)