import sys
input = sys.stdin.readline

# tree dp를 그리는 dfs
def dfs(cur_node):
    visited[cur_node] = True
    dp[cur_node][0] = node_v[cur_node]
    dp[cur_node][1] = 0
    for next_node in tree[cur_node]:
        if not visited[next_node]:
            dfs(next_node)
            dp[cur_node][0] += dp[next_node][1]
            dp[cur_node][1] += max(dp[next_node][0],dp[next_node][1])

# pre_node의 존재 유무에 따라 분기를 타는 trace
def trace(cur_node,pre_node):
    trace_visited[cur_node] = True

    if not pre_node:
        for next_node in tree[cur_node]:
            if not trace_visited[next_node]:
                trace(next_node,1)
    else:
        if dp[cur_node][0] > dp[cur_node][1]:
            trace_res.append(cur_node)
            for next_node in tree[cur_node]:
                if not trace_visited[next_node]:
                    trace(next_node,0)
        else:
            for next_node in tree[cur_node]:
                if not trace_visited[next_node]:
                    trace(next_node,1)


n = int(input())
node_v = [0] + list(map(int,input().split()))
tree = {i: [] for i in range(1,n+1)}
dp = {i: [0,0] for i in range(1,n+1)}

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a] += [b]
    tree[b] += [a]

visited = {i: False for i in range(1,n+1)}
dfs(1)
print(max(dp[1][0],dp[1][1]))
trace_res = []
trace_visited = {i: False for i in range(1,n+1)}
trace(1,1)
trace_res.sort()
print(*trace_res)