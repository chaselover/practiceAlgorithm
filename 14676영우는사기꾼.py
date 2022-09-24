import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
graph = {i: [] for i in range(1,N+1)}
level = {i: 0 for i in range(1,N+1)}
built = {i:0 for i in range(1,N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    level[b] += 1

for _ in range(K):
    command, building = map(int, input().split())
    if command==1:
        if not level[building]:
            built[building] += 1
            if built[building]==1:
                for next in graph[building]:
                    level[next] -= 1
        else:
            print('Lier!')
            exit()
    else:
        if built[building] >=1:
            built[building] -= 1
            if not built[building]:
                for next in graph[building]:
                    level[next] += 1
        else:
            print('Lier!')
            exit()

print('King-God-Emperor')
