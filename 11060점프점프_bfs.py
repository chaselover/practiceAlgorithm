n = int(input())
lst = list(map(int, input().split()))

dp = [-1] * n

def bfs(start):
    q = []
    q.append(start)
    dp[start] = 0
    while q:
        v = q.pop(0)
        jump = lst[v]
        for i in range(jump, 0, -1):
            if v + i < n and dp[v + i] == -1:
                dp[v + i] = dp[v] + 1
                q.append(v + i)

bfs(0)
print(dp[-1])