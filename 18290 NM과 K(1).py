def dfs(now_i, now_j, level, now_sum):
    if level == K:
        global res
        res = max(res, now_sum)
        return
    
    for near_i, near_j in near_idx:
        temp_i, temp_j = now_i+near_i, now_j+near_j
        if temp_i<N and temp_j<M:
            near_check[temp_i][temp_j] += -1

    for j in range(now_j+1, M):
        if near_check[now_i][j] == 0:
            dfs(now_i, j, level+1, now_sum+grid[now_i][j])

    for i in range(now_i+1, N):
        for j in range(M):
            if near_check[i][j] == 0:
                dfs(i, j, level+1, now_sum+grid[i][j])
    
    for near_i, near_j in near_idx:
        temp_i, temp_j = now_i+near_i, now_j+near_j
        if temp_i<N and temp_j<M:
            near_check[temp_i][temp_j] += 1

if __name__ == "__main__":
    N, M, K = map(int, input().rstrip().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().rstrip().split())))

    near_idx = [[0, 1], [1, 0]]
    near_check = [[0]*M for _ in range(N)]
    res = -40001
    for start_i in range(N):
        for start_j in range(M):
            dfs(start_i, start_j, 1, grid[start_i][start_j])
    print(res)


################################################################
def dfs(x, y, cnt, sum_value):
    global max_value
    if cnt == k:
        max_value = max(max_value, sum_value)
        return
    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if check[i][j]:
                continue
            for dx, dy in dxy:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and check[nx][ny]:
                    break
            else:
                check[i][j] = True
                dfs(i, j, cnt + 1, sum_value + item[i][j])
                check[i][j] = False


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    item = []
    for _ in range(n):
        item.append(list(map(int, input().split())))

    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    max_value = 0
    check = [[False for _ in range(m)] for _ in range(n)]
    dfs(0, 0, 0, 0)
    print(max_value)


##############################
n, m, k = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(n)]
INF = 10**7
MASK = (1<<m)-1

dp = [[-INF]*(1<<m) for ch in range(k+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(m):
        new = [[-INF]*(1<<m) for ch in range(k+1)]
        for ch in range(k+1):
            for bit in range(1<<m):
                nbit = (bit<<1)&MASK
                new[ch][nbit] = max(new[ch][nbit], dp[ch][bit])
                if ch == k: continue
                if j>0 and bit&(1 | (1<<(m-1))): continue
                if j==0 and bit&(1<<(m-1)): continue
                nval = dp[ch][bit] + grid[i][j]
                new[ch+1][nbit|1] = max(new[ch+1][nbit|1], nval)
        dp = new
print(max(dp[k]))
