from _collections import deque
 
 
def check(a, b):
    return True if 0 <= a < n and 0 <= b < n else False
 
 
if  __name__ == "__main__":
 
    for tc in range(1, int(input())+1):
        n = int(input())
        matrix = [list(map(int, input())) for _ in range(n)]
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]
        # visit = [[0] * n for _ in range(n)]
 
        cost[0][0] = 0
        queue = deque()
        queue.append((0, 0))
        # visit[0][0] = 1
 
        while queue:
            cr, cc = queue.popleft()
 
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr = dr + cr
                nc = dc + cc
 
                if check(nr, nc) and cost[nr][nc] > matrix[nr][nc] + cost[cr][cc]:
                    cost[nr][nc] = matrix[nr][nc] + cost[cr][cc]
                    # visit[nr][nc] = 1
                    queue.append((nr, nc))
 
 
        print("#{} {}".format(tc, cost[n-1][n-1]))