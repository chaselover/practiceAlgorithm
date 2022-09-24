from collections import deque
 
dx = [0,0,1,-1]
dy = [1,-1,0,0]
 
def dfs(x,y):
    q = deque()
    q.append((x,y))
    d[x][y] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if d[nx][ny] == -1:
                    d[nx][ny] = d[x][y]+a[nx][ny]
                    q.append((nx,ny))
                else:
                    if d[nx][ny] > d[x][y]+a[nx][ny]:
                        d[nx][ny] = d[x][y]+a[nx][ny]
                        q.append((nx,ny))
                    else:
                        continue
for t in range(int(input())):
    n = int(input())
    a = [list(map(int,list(input()))) for _ in range(n)]
    d = [[-1]*(n) for _ in range(n)]
    dfs(0,0)
    print('#{} {}'.format(t+1,d[n-1][n-1]))