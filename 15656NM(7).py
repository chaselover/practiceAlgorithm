def dfs(depth):
    if depth==M:
        print(*ans)
        return
    for i in range(N):
            ans.append(lis[i])
            #탐색 start값을 i보다 큰값으로 주겠다.
            dfs(depth+1)
            ans.pop()
    
N,M = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
ans = []
dfs(0)