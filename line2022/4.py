from typing import List
from collections import deque


delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (-2, 0), (0, 2), (0, -2), (0, 3), (0, -3), (-1, 1), (-1, -1))

def solution(wall: List[str]):
    n = len(wall)
    m = len(wall[0])
    cnts = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((n - 1, 0))
    cnts[n - 1][0] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and wall[nx][ny] == 'H' and cnts[nx][ny] == 0:
                if dx == -2 and wall[x - 1][y] == '.':
                    queue.append((nx, ny))
                elif dy == 2 and wall[x][y + 1] == '.' and x - 1 >= 0 and wall[x - 1][y + 1] == '.':
                    queue.append((nx, ny))
                elif dy == -2 and wall[x][y - 1] == '.' and x - 1 >= 0 and wall[x - 1][y - 1] == '.':
                    queue.append((nx, ny))
                elif dy == -3 and wall[x][y - 1] == '.' and x - 1 >= 0 and wall[x - 1][y - 1] == '.' and wall[x][y - 2] == '.' and wall[x - 1][y - 2] == '.':
                    queue.append((nx, ny))
                elif dy == 3 and wall[x][y + 1] == '.' and x - 1 >= 0 and wall[x - 1][y + 1] == '.' and wall[x][y + 2] == '.' and wall[x - 1][y + 2] == '.':
                    queue.append((nx, ny))
                elif dx == -1 and dy == 1 and wall[x][y + 1] == '.' and wall[x - 1][y] == '.':
                        queue.append((nx, ny))
                elif dx == -1 and dy == -1 and wall[x][y - 1] == '.' and wall[x - 1][y] == '.':
                        queue.append((nx, ny))
                elif abs(dx + dy) == 1:
                    queue.append((nx, ny))
                else:
                    continue
                cnts[nx][ny] = cnts[x][y] + 1
    
    for i in range(n):
        for j in range(m):
            if wall[i][j] == 'H' and cnts[i][j] == 0:
                cnts[i][j] = -1
    return cnts



print(solution(["H.H", ".HX", "H.H"]))