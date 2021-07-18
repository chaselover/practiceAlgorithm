def dfs(start,depth):
    if depth==M:
        print(*ans)
        return
    for i in range(start,N):
        if not check[i]:
            check[i] = 1
            ans.append(lis[i])
            dfs(i+1,depth+1)
            ans.pop()
            check[i]=0
    
N,M = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
check = [0]*N
ans = []
dfs(0,0)