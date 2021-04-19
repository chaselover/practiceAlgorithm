





N, M = map(int, input().split())
matrix = []
check = [[0]*M for _ in range(N)]
max_distance = 0
for _ in range(N):
    matrix.append(list(input()))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(x,y):
    stack = []
    check[x][y] = 1
    stack.append([x,y])
    while stack:
        x,y = stack.pop()
        if x == N-1 and y == M-1:
            if len(stack)<max_distance:
                max_distance = len(stack)
            return max_distance
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and matrix[nx][ny]==0 and check[nx][ny] == 0:
                stack.append([nx,ny])
                check[nx][ny] =1



print(DFS(0,0))