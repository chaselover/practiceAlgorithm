import sys

INF = 10**18

n, m = map(int, sys.stdin.readline().split())

tr = [[] for _ in range(n+1)]
dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    dist[i][i] = 0

for _ in range(m):
    u , v, b = map(int , sys.stdin.readline().split())
    # 여기가 핵심. 길을 바꿔야 하는 길은 가중치 1을 주는 것.
    if b==0:
        dist[u][v] = 0
        dist[v][u] = 1
    else:
        dist[u][v] = 0
        dist[v][u] = 0

#연결이 되어있으면 비용이 0, 연결이 될수있는곳은 비용 1, 연결이 불가능한곳은 inf
#최종 비용이 0이면 무료, 최종 비용이 1이상이면 길 바꿔야함을 의미한다고 하자


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

k = int(sys.stdin.readline())

# 일단 쿼리가 여러개면 플로이드 워셜 의심 해야함.
for _ in range(k):
    s, e = map(int, sys.stdin.readline().split())
    print(dist[s][e])
