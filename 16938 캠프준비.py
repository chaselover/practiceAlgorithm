import sys
input = sys.stdin.readline

def dfs(idx, s, min_n, max_n):
    global cnt
    if L <= s <= R and max_n - min_n >= X:
        cnt += 1
    if s > R:
        return
    for next_idx in range(idx+1,N):
        dfs(next_idx, s+arr[next_idx], min(min_n, arr[next_idx]), max(max_n, arr[next_idx]))
N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
dfs(-1, 0, float('inf'), 0)
print(cnt)