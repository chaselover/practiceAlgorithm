def dfs(depth):
    if depth==M:
        print(*ans)
        return
    same = 0
    for i in range(N):
        if not check[i] and same != lis[i]:
            ans.append(lis[i])
            check[i] = True
            same = lis[i]
            dfs(depth+1)
            ans.pop()
            check[i] = False
    # 9,9가 되는 이유는 뒤의 9의 전값은 9가 아니라 7이기 때문(7탐색후 9탐색을 들어갔기 때문에.)
N,M = map(int,input().split())
lis = list(map(int,input().split()))

lis.sort()
check = [False]*N
ans = []

dfs(0)
