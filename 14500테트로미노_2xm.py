import sys
input = sys.stdin.readline

def DFS(x,y,sum_t,depth):
    global max_sum
    if depth==4:
        max_sum = max(sum_t,max_sum)
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = True
            DFS(nx,ny,sum_t+matrix[nx][ny],depth+1)
            visited[nx][ny] = False

def hat(x,y):
    global max_sum
    for idxs in hat_idx:
        try:
            max_sum = max(max_sum,matrix[x][y]+matrix[x+idxs[0][0]][y+idxs[0][1]]+matrix[x+idxs[1][0]][y+idxs[1][1]] + matrix[x+idxs[2][0]][y+idxs[2][1]])
        except:
            continue

# DFS로 4칸 조사(출발지에서 위, 왼쪽, 위대각왼쪽, 왼대각아래는 제외). 빠큐모양 따로조사(4가지).
N,M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
max_sum = 0
visited = [[False]*(M+1) for _ in range(N+1)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

hat_idx = [[[1,0],[1,1],[2,0]],[[1,0],[1,-1],[2,0]],[[0,1],[-1,1],[0,2]],[[0,1],[1,1],[0,2]]]

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i,j,matrix[i][j],1)
        visited[i][j] = False
        hat(i,j)

print(max_sum)