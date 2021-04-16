import sys




col,row = map(int,sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split()))for _ in range(col)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
check = [[-1]*row for _ in range(col)]
check[0][0] =0

def dfs(x,y):
    cnt = 0
    if x==col-1 and y==row-1: #경로찾으면 1만 반환하고 함수 끝나는게 아님.
        return 1
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if 0<=X<col and 0<=Y<row:
            if matrix[x][y]>matrix[X][Y]:
                if check[X][Y] >=0:
                    cnt += check[X][Y]
                else:
                    cnt += dfs(X,Y)
    check[x][y] = cnt
    return cnt #최종 긑나면 cnt반환까지 해줘야함.
cnt = dfs(0,0)
print(cnt)
                

# 결국 아이디어는 미로찾기에서 경로의 수와 비슷함. 모서리마다 경우의 수를 더하여 
# 사거리, 삼거리 , 골목길에서는 각 모서리들의 경우의 수의 합을 하다보면 최종 도착 시 경우의 수가 나옴.