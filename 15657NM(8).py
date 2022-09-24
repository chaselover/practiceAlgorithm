def dfs(start,depth):
    if depth==M:
        print(*ans)
        return
    for i in range(start,N):
            ans.append(lis[i])
            dfs(i,depth+1)
            ans.pop()
    
N,M = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
ans = []
dfs(0,0)