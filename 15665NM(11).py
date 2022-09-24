import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list(map(int,input().split()))
ans =[]
nums.sort()
# 같은수 여러번 

def dfs(depth):
    if depth == M:
        print(*ans)
        return
    same = 0
    for i in range(N):
        if same != nums[i]:
            ans.append(nums[i])
            same = nums[i]
            dfs(depth+1)
            ans.pop()

dfs(0)