import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
check = [False] * 1000
ans = []

def DFS(v,cnt):
    if v>=N-1:
        ans.append(cnt)
        return
    if A[v]==0:
        return
    for i in range(1,A[v]+1):
        if not check[v+i]:
            check[v+i] = True
            DFS(v+i,cnt+1)
            check[v+i] = False

check[0]=True
DFS(0,0)
if ans:
    print(min(ans))
else:
    print(-1)