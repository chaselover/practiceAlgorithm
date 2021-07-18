import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
check = [False] * 1200
ans = []
v = 0
cnt = 0
def DFS(v,cnt):
    if v>=N-1:
        ans.append(cnt)
        return
    if A[v]==0:
        return
    for i in range(1,A[v]+1):
        if not check[v+i] and not v+i>N-1:
            check[v+i] = True
            DFS(v+i,cnt+1)
            check[v+i] = False

check[0]=True
DFS(0,0)
print(min(ans) if ans else -1)