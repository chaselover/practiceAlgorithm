import sys
input = sys.stdin.readline

def DFS(depth,start,sum_t):
    if depth==3:
        if arr[start]==sum_t:
            return True
        return
    for pre_num in arr[:start]:
        if DFS(depth+1,start,sum_t+pre_num):
            return True

N = int(input())
arr = list(map(int,input().split()))

# 앞에있는 수 3개의 합. DFS(중복가능) depth 3까지.
cnt=0
for i in range(1,N):
    if DFS(0,i,0):
        cnt+=1
print(cnt)
    