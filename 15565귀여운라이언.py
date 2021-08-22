import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

left = 0
lion_cnt = 0
min_size = float('inf')
for right in range(N):
    
    if dolls[right]==1:
        lion_cnt += 1
        if lion_cnt==1:
            left = right
    while lion_cnt > K:
        left += 1
        if dolls[left]==1:
            lion_cnt -= 1
    if lion_cnt == K:
        min_size = min(min_size,right-left+1)
if min_size==float('inf'):
    print(-1)
else:
    print(min_size)
