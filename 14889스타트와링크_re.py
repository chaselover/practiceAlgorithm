import sys
input = sys.stdin.readline

def DFS(start,depth):
    global ans
    if depth==N//2:
        start,link=0,0
        for i in range(N-1):
            for j in range(i+1,N):
                if visited[i] and visited[j]:
                    start += sinerge[i][j] + sinerge[j][i]
                elif not visited[i] and not visited[j]:
                    link += sinerge[i][j] + sinerge[j][i]
        ans = min(ans,abs(start-link))
    for i in range(start,N):
        if not visited[i]:
            visited[i] = True
            DFS(i+1,depth+1)
            visited[i] = False

N = int(input())
sinerge = [list(map(int,input().split())) for _ in range(N)]

# 팀에i,j가 속하면 능력치는 sinerge[i][j] + sinerge[j][i] 다 가져감.
# 모든 원소를 두 집단으로 나눠 차이를 최소로 할때 차이의 최솟값은?
# 일단 두 집단으로 나누는 경우의 수. N개중에 N//2개를 뽑는 조합.
# DFS로 depth N//2까지 탐색. sum구하고 차이 저장.

visited = [False]*N
ans=float('inf')
DFS(0,0)
print(ans)