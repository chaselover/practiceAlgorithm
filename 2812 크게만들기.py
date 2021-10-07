import sys
input = sys.stdin.readline

N , K = map(int,input().split())
nums = list(input().rstrip())
answer = []

for i in range(N):
    while K != 0 and answer:
        if answer[-1] < nums[i]:
            answer.pop()
            K -= 1
        else: break
    answer.append(nums[i])
if K: answer = answer[:-K]
print(''.join(answer))