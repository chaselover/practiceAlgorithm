import sys,collections
input = sys.stdin.readline


N,K = map(int,input().split())
nums = [i for i in range(1,N+1)]
answer = []

for i in range(N*K):
    if i%K==K-1:
        answer.append(nums[i%N])
        del nums[i%N]
    if not nums:
        break


answer = ', '.join(list(map(str,answer)))
print(f"<{answer}>")


