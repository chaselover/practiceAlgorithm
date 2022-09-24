import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list(map(int,input().split()))
ans =[]
check = [False]*N
nums.sort()
# 중복 x 비내림차순 조합..

def dfs(start,depth):
    if depth == M:
        print(*ans)
        return
    same = 0
    for i in range(start,N):
        if not check[i] and same != nums[i]:
            ans.append(nums[i])
            check[i] = True
            same = nums[i]
            dfs(i+1,depth+1)
            check[i]=False
            ans.pop()

dfs(0,0)