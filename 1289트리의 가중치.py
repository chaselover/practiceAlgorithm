import sys
input =sys.stdin.readline
sys.setrecursionlimit(10**6)

# dp[u]는 노드 u가 루트인 subtree에서 u부터 다른 모든 노드 까지 가는 모든 경로들의 곱의 합.
# 즉 (dp[v] * c) 들의 합. 그 값을 리스트 p에 저장해뒀다가 모든 값들에 대해 (dp[u] - dp[v]*c)*(c*dp[v])들의 합을 구해준다.
# 그 후 중복을 제거하기 위해 나누기 2를 해줘야 하나 MOD의 반인 500000004를 곱하고 MOD로 나눔으로써 2로 나누는 것과 같은 효과를 얻을 수 있다.
def dfs(u):
    global ans
    visited[u] = True
    p = []
    for i in range(len(edges[u])):
        v = edges[u][i]
        c = costs[u][i]
        if visited[v]:
            continue

        dfs(v)
        dp[u] += (dp[v] * c) % MOD
        dp[u] %= MOD

        p.append((dp[v] * c) % MOD)
    ans += dp[u]
    ans %= MOD

    sum_v = 0
    # (ab+ac+ad+bc+bd+cd) = ((a+b+c+d)^2-(a^2+b^2+c^2+d^2))/2 를 사용해 시간복잡도를 O(n^2)에서 O(n)으로 바꿈.
    for v in p:
        sum_v += ((dp[u] - v + MOD) % MOD * v) % MOD
        sum_v %= MOD
    
    sum_v *= 500000004
    sum_v %= MOD
    
    ans += sum_v
    ans %= MOD                

    dp[u] += 1
    dp[u] %= MOD


MOD = 1000000007
N = int(input())
ans = 0
visited = {i: False for i in range(1,N+1)}
dp = [0 for _ in range(N+1)]
edges = {i: [] for i in range(1,N+1)}
costs = {i: [] for i in range(1,N+1)}
for _ in range(N-1):
    a, b, c = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
    costs[a].append(c)
    costs[b].append(c)

dfs(1)
print(ans)


# 다른사람 코드
import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
mod = 1000000007
adj = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
ans = 0
def go(now, past):
    global ans
    pow = 1
    for i in adj[now]:
        next = i[0]
        next_cost = i[1]
        if next != past:
            extra_cost = (go(next, now) * next_cost) % mod
            ans = (ans + extra_cost * pow) % mod
            pow = (pow + extra_cost) % mod
    return pow

go(1,-1)
print(ans)