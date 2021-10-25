import sys
input = sys.stdin.readline
from collections import deque


def rotate_dice(d):
    if d == 0:
        dice['top'], dice['left'], dice['bottom'], dice['right'] = dice['left'], dice['bottom'], dice['right'], dice['top']
    elif d == 1:
        dice['top'], dice['up'], dice['bottom'], dice['down'] = dice['up'], dice['bottom'], dice['down'], dice['top']
    elif d == 2:
        dice['left'], dice['bottom'], dice['right'], dice['top'] = dice['top'], dice['left'], dice['bottom'], dice['right']
    else:
        dice['up'], dice['bottom'], dice['down'], dice['top'] = dice['top'], dice['up'], dice['bottom'], dice['down']


def bfs(x, y, pivot):
    q = deque()
    q.append((x, y))
    cnt = 1
    visited = set()
    visited.add((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == pivot and (nx, ny) not in visited:
                visited.add((nx, ny))
                cnt += 1
                q.append((nx, ny))
    return cnt * pivot


def move(x, y, k):
    global answer
    q = []
    q.append((x, y, 0))
    while k:
        x, y, direction = q.pop()
        nx, ny = x + delta[direction][0], y + delta[direction][1]
        if nx < 0 or nx >= N:
            direction = (direction + 2) % 4
            nx, ny = x + delta[direction][0], y + delta[direction][1]
        elif ny < 0 or ny >= M:
            direction = (direction + 2) % 4
            nx, ny = x + delta[direction][0], y + delta[direction][1]
        # 방향성에 따라 주사위 회전
        rotate_dice(direction)
        # bfs answer갱신
        answer += bfs(nx, ny, maps[nx][ny])
        # bottom값과 map값 사이 비교 후 방향 수정
        if dice['bottom'] > maps[nx][ny]:
            direction = (direction + 1) % 4
        elif dice['bottom'] < maps[nx][ny]:
            direction = (direction - 1) % 4
        q.append((nx, ny, direction))
        k -= 1


N, M, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dice = {'up': 2, 'left': 4, 'top': 1, 'right': 3, 'down': 5, 'bottom': 6}
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
answer = 0

# 이동
move(0, 0, K)
print(answer)


