import heapq
 
def dijkstra(lst, n, r, c):
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]
    distances[r][c] = 0
    queue = []
    heapq.heappush(queue, [0, r, c])
    while queue:
        current_distance, y, x = heapq.heappop(queue)
        if distances[y][x] < current_distance:
            continue
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                distance = current_distance + int(lst[ny][nx])
                if distance < distances[ny][nx]:
                    distances[ny][nx] = distance
                    heapq.heappush(queue, [distance, ny, nx])
    return distances[n-1][n-1]
 
T = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    print('#{} {}'.format(test_case, dijkstra(lst, N, 0, 0)))
