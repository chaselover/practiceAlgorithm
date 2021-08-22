import sys
input = sys.stdin.readline

def DFS(cnt,dduks,yesterday):
    global answer
    if cnt == N:
        for d in dduks:
            print(d)
        exit()
    for dduk in days[cnt]:
        if dduk != yesterday and not ate[cnt][dduk-1]:
            ate[cnt][dduk-1] = True
            DFS(cnt+1, dduks + [dduk],dduk)

N = int(input())
days = []
answer = []
for _ in range(N):
    m,*dduk = map(int, input().split())
    days.append(dduk)
ate = {i:[False for _ in range(10)] for i in range(N+1)}
DFS(0,[],0)
print(-1)