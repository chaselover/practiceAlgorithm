import sys
input = sys.stdin.readline

n = int(input())
nums=sorted([int(input()) for _ in range(n)], reverse=True)
answer = 0
for i in range(n):
    if not i % 3 == 2 :
        answer += nums[i]
print(answer)