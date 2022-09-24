import sys
input = sys.stdin.readline

def find(now,before):
    if dp[now][before]:
        return dp[now][before]
    if before == (1<<N)-1:
        if dists[now][0]>0:
            return dists[now][0]
        else:
            return float('inf')
    cost = float('inf')
    for i in range(1,N):
        if not (before>>i)%2 and dists[now][i]:
            tmp = find(i,before|(1<<i))
            cost = min(cost,tmp+dists[now][i])
    dp[now][before] = cost
    return cost

N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
dists = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i,N):
        dists[i][j] = ((maps[i][0]-maps[j][0])**2 + (maps[i][1]-maps[j][1])**2)**0.5
        dists[j][i] = ((maps[i][0]-maps[j][0])**2 + (maps[i][1]-maps[j][1])**2)**0.5
dp = [[0]*(1<<N) for _ in range(N)]

answer = find(0,1)
print(answer)