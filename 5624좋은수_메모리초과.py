import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

sums=[[],[],[]]
# 앞의 모든 수를 더하는 집합 set을 만들어보자.
for i in range(N-1):
    sums[0].append(arr[i])
    for sum_num in sums[0]:
        sums[1].append(sum_num+arr[i])
    for sum_num in sums[1]:
        sums[2].append(sum_num+arr[i])
cnt=0
for i in range(1,N):
    if arr[i] in sums[2]:
        cnt+=1

print(cnt)
