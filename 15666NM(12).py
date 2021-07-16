import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list(map(int,input().split()))
ans =[]
nums.sort()
# 중복 x 비내림차순 조합..

def dfs(start,depth):
    if depth == M:
        print(*ans)
        return
    same = 0
    for i in range(start,N):
        if same != nums[i]:
            ans.append(nums[i])
            same = nums[i]
            # i +1안해주면 자기자신부터 시작(중복가능)
            dfs(i,depth+1)
            ans.pop()

dfs(0,0)