N,M=map(int,input().split())
arr=[list(map(str,input()))for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dy=[0,0,1,-1]
dx=[1,-1,0,0]
flag=False
def scope(y,x):
    if y>=0 and y<N and x>=0 and x<M:
        return True
    else:
        return False
 
def dfs(y,x,py,px,ball):
    if visited[y][x]==1:
        return True
    visited[y][x]=True
 
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if ny!=py or nx!=px:
            if scope(ny,nx) and arr[ny][nx]==ball :
                if dfs(ny,nx,y,x,ball): return True
    return False
 
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        if dfs(i,j,0,0,arr[i][j]):
            flag=True
            break    
print("Yes") if flag else print("No")