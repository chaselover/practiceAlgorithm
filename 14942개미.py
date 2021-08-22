import sys, heapq

# INF : 무한대값
INF = 10000000000000000000000

# 입력부
n = int(sys.stdin.readline())
ant = []
for i in range(n):
    temp = int(sys.stdin.readline())
    ant.append(temp)
    
# 인접 리스트 생성
adj = [[] for _ in range(n)]
for i in range(n - 1):
    a,b,c = map(int, sys.stdin.readline().split())
    adj[a - 1].append((b - 1, c))
    adj[b - 1].append((a - 1, c))

# ans : 정답배열, 1번 방에 사는 개미는 항상 1번이 제일 가까우므로 1을 넣고 시작
ans = [1]

# dijstra : 다익스트라 알고리즘 + path 갱신
def dijstra(v):
    d[v] = 0
    min_q = []
    min_q.append((d[v], v))
    while len(min_q) != 0:
        distance = min_q[0][0]
        current = min_q[0][1]
        heapq.heappop(min_q)
        if d[current] < distance:
            continue
        for i in range(len(adj[current])):
            next = adj[current][i][0]
            nextdistance = adj[current][i][1] + distance
            if nextdistance < d[next]:
                d[next] = nextdistance
                # next에서 인접한 방들 중 가장 짧은 거리는 current다
                path[next].append(current)
                heapq.heappush(min_q, (nextdistance, next))

d = [INF] * n
path = [[] for _ in range(n)]

# 1번방 기준 다익스트라
dijstra(0)
for i in range(1,n):
    for j in adj[i]:
        # 만일 최단 거리 방이 맞다면, 그때의 에너지 소모량도 같이 저장한다
        if j[0] == path[i][0]:
            path[i].append(j[1])

# 1번 방의 경우 예외처리
path[0] = [0,0]

for i in range(1, n):
    energy = ant[i]
    route = i
    # 지속적으로 path 배열을 타고 올라가다가 에너지가 0이하가 되면 정답 리턴
    while True:
        energy -= path[route][1]
        if energy < 0:
            ans.append(route + 1)
            break
        elif route == 0:
            ans.append(route + 1)
            break
        route = path[route][0]

# 정답 출력
for i in ans:
    print(i)