"""
출발S(0,0), 도착G(n-1,n-1)
깊이D에 비례하는 시간t
min(sum(t))=??


"""
def findway_DFS(x,y,cnt):
    check[x][y]=1

    for i in range(4):
        X = x +dx[i]
        Y = y +dy[i]
        if 0<=X<N and 0<=Y<N and check[X][Y] == 0:
            cnt += map[X][Y]
            cnt = findway_DFS(X,Y,cnt)

        if x ==N-1 and y==N-1 :
            path.append(cnt)
            return cnt
    




T = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for test in range(1,T+1):
    N = int(input())
    map = [list(map(int,input())) for _ in range(N)]
    check = [[0]*N for _ in range(N)]
    min=float('inf')
    cnt = 0
    findway_DFS(0,0,0)
    print(f"#{test} {min(path)}")
