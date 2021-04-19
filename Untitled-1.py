import heapq


V, E = map(int,input().split())
start_node = int(input())
graph = [[]*V for _ in range(V+1)]
distance = [float('inf')]*(V+1)


for _ in range(E):
    i,j,k = map(int,input().split())
    graph[i].append((j,k))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0,start_node))
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue
        for adj in graph[node]:
            cost  = dist + adj[1]
            if cost < distance[adj[0]]:
                distance[adj[0]] = cost
                heapq.heappush(queue, (cost,adj[0]))


dijkstra(start_node)

for i in range(1, V + 1):
    if distance[i] == float('inf'):
        print("INFINITY")
    else:
        print(distance[i])