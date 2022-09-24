import sys
input = sys.stdin.readline

# 파티 만족도 : 파티동안 먹은 모든 간식의 평점 합 / 

N = int(input())
scores = [int(input()) for _ in range(N)]
dp = [scores[i] for i in range(N)]
for i in range(1,N):
    tmp=[0]
    for j in range(i):
        if scores[j] < scores[i]:
            tmp.append(dp[j])
    dp[i] = max(tmp) + scores[i]
print(max(dp))
