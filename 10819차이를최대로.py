import sys
input  = sys.stdin.readline
from itertools import permutations

N = int(input())
A = list(map(int,input().split()))
p = permutations(A)
ans = []
for nums in p:
    sum_nums = 0
    for i in range(0,len(nums)-1):
        sum_nums += abs(nums[i]-nums[i+1])
    ans.append(sum_nums)

print(max(ans))