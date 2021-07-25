
def DFS(depth):
    if depth == M:
        print(*ans)
        return
    for i in range(N):
        if not checks[i]:
            checks[i] = 1
            ans.append(nums[i])
            DFS(depth+1)
            ans.pop()
            checks[i] = 0

N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
checks = [0 for _ in range(N)]
ans = []
DFS(0)