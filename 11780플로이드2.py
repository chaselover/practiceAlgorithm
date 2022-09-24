import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
cities = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
pre_node = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    cities[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    cities[a][b] = min(cities[a][b],c)
    # 이전노드 저장.
    pre_node[a][b] = a

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if cities[i][j] > cities[i][k] + cities[k][j]:
                cities[i][j] = cities[i][k] + cities[k][j]
                pre_node[i][j] = pre_node[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        print(cities[i][j] if not cities[i][j]==float('inf') else 0,end=" ")
    print()
# i 에서 j로 가는 최소비용에 포함되어 잇는 도시의 개수 k출력
# i에서 j로 가는 경로를 공배으로 구분해 출력.
for i in range(1,n+1):
    for j in range(1,n+1):
        if cities[i][j]==float('inf') or cities[i][j]==0:
            print(0)
        else:
            # i에서 경로를 따라 최단거리를 추적하는 노드들.
            path = [j]
            end_point = j
            while end_point != i:
                path.append(pre_node[i][end_point])
                end_point = pre_node[i][end_point]
            print(len(path), end=" ")
            print(*path[::-1])
