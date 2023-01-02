import sys
sys.setrecursionlimit(10**6)

dr = [0, 1, 0,-1]
dc = [1, 0,-1, 0]

def dfs(r ,c):
    global state, visited
    if not(0<=r<N and 0<=c<M) or board[r][c] == 'H':
        return 0
    if visited[r][c]:
        state = True
        return -1
    if dp[r][c] != -1:
        return dp[r][c]

    visited[r][c] = True
    X = int(board[r][c])
    for i in range(4):
        dp[r][c] = max(dp[r][c], dfs(r+dr[i]*X, c+dc[i]*X)+1)
        if state:
            return -1
    visited[r][c] = False
    
    return dp[r][c]

if __name__ == '__main__':

    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    dp = [[-1]*M for _ in range(N)]
    state = False
    print(dfs(0,0))