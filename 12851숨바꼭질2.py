import sys
from collections import deque
input = sys.stdin.readline

n, k = list(map(int, input().split()))

def bfs(n):
    # visited[next] : next 까지 오는데 얼마의 최소 time을 저장.
    # ways[next] : next 까지 최소 time으로 오는 방법의 수 저장.
    queue = deque([n])
    visited = [float('inf')]*100001
    ways = [0]*100001
    time = 0
    success = False
    ways[n] = 1
    visited[n] = 0

# 한 size씩 측정해 그 사이즈까지만 돌리고 성공했으면 빠져나옴.
    while queue and not success:
        size = len(queue)

        for _ in range(size):
            v = queue.popleft()

            for next in [v-1, v+1, v*2]:
                if 0<= next <= 100000 and time + 1 <= visited[next]:
                    ways[next] += 1
                    visited[next] = time + 1

                    if next == k:
                        success = True

                    if not success:
                        queue.append(next)
        time += 1

    return visited[k], ways[k]
if n >= k:
    print(n-k)
    print(1)
else:
    time, count = bfs(n)
    print(time)
    print(count) 