import sys
input = sys.stdin.readline

K,N = map(int,input().split())
lengths = []
for _ in range(K):
    lengths.append(int(input()))

start = 1
end = 2**31-1
answer = 0
mid = 0

while start <=end:
    mid = (start+end)//2
    count=0
    for i in range(K):
        count+=lengths[i]//mid
    if count>=N:
        answer = mid
        start = mid+1
    else:
        end = mid-1
print(answer)
