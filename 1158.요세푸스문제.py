import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = [i for i in range(1, N + 1)]

result = []
idx = 0
for _ in range(N):
    idx += K-1
    if len(nums) <= idx:
        idx %= len(nums)
    result.append(nums[idx])
    nums = nums[:idx]+nums[idx+1:]
    
ended=[]
ended.append(result.pop())
ended.append(">")
if N==1:
    print("<1>")
else:
    print("<", end='')
    print(*result,sep=', ',end = ', ')
    print(*ended,sep='')
