from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def spread_temperature():
    for warmer in warmers:
        q = deque()
        x, y = warmer
        d = warmers[warmer]
        nx, ny = x + delta[d][0], y + delta[d][1]
        q.append((nx, ny))
        visited = set()
        rooms[nx][ny] += 5
        level = 4
        while q and level:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in winds[d]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in visited and (nx, ny) not in walls[d][(x, y)]:
                        visited.add((nx, ny))
                        q.append((nx, ny))
                        rooms[nx][ny] += level
            level -= 1
            if not level:
                break


def warmming_house():
    new_board = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if rooms[x][y] >= 4:
                for i in range(4):
                    nx, ny = x + delta[i][0], y + delta[i][1]
                    if 0 <= nx < R and 0 <= ny < C and rooms[x][y] > rooms[nx][ny]:
                        if (nx, ny) in walls[i][(x, y)]:
                            continue
                        unit = (rooms[x][y] - rooms[nx][ny]) // 4
                        new_board[nx][ny] += unit
                        new_board[x][y] -= unit
    for i in range(R):
        for j in range(C):
            rooms[i][j] += new_board[i][j]


def down_boundary():
    for i in range(R):
        for j in (0, C - 1):
            if rooms[i][j]:
                rooms[i][j] -= 1
    for i in (0, R - 1):
        for j in range(1, C - 1):
            if rooms[i][j]:
                rooms[i][j] -= 1


def checking():
    for x, y in list(check):
        if rooms[x][y] >= K:
            check.discard((x, y))


R, C, K = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(R)]
W = int(input())

right = defaultdict(set)
left = defaultdict(set)
up = defaultdict(set)
down = defaultdict(set)
walls = {idx: name for idx, name in enumerate([right, left, up, down])}
for _ in range(W):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t:
        walls[0][(x, y)].add((x, y + 1))
        walls[0][(x - 1, y)].add((x, y + 1))
        walls[0][(x + 1, y)].add((x, y + 1))
        walls[1][(x, y + 1)].add((x, y))
        walls[1][(x - 1, y + 1)].add((x, y))
        walls[1][(x + 1, y + 1)].add((x, y))
        walls[2][(x, y + 1)].add((x - 1, y))
        walls[2][(x, y)].add((x - 1, y + 1))
        walls[3][(x, y + 1)].add((x + 1, y))
        walls[3][(x, y)].add((x + 1, y + 1))
    else:
        walls[0][(x, y)].add((x - 1, y + 1))
        walls[0][(x - 1, y)].add((x, y + 1))
        walls[1][(x, y)].add((x - 1, y - 1))
        walls[1][(x - 1, y)].add((x, y - 1))
        walls[2][(x, y)].add((x - 1, y))
        walls[2][(x, y - 1)].add((x - 1, y))
        walls[2][(x, y + 1)].add((x - 1, y))
        walls[3][(x - 1, y)].add((x, y))
        walls[3][(x - 1, y - 1)].add((x, y))
        walls[3][(x - 1, y + 1)].add((x, y))

winds = {
    0: [(-1, 1), (0, 1), (1, 1)], 
    1: [(-1, -1), (0, -1), (1, -1)], 
    2: [(-1, -1), (-1, 0), (-1, 1)],
    3: [(1, 1), (1, 0), (1, -1)],
     }
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
warmers = {}
check = set()
for i in range(R):
    for j in range(C):
        if rooms[i][j] == 5:
            check.add((i, j))
        elif rooms[i][j]:
            warmers[(i, j)] = rooms[i][j] - 1
        rooms[i][j] = 0

cnt = 0
while len(check):
    # 온풍기에서 바람이 한번씩 나온다.
    spread_temperature()
    # 온도 조절
    warmming_house()
    # 가장 바깥쪽 칸의 온도 1씩 감소
    down_boundary()
    # 초콜릿 1개 먹기
    cnt += 1
    if cnt > 100:
        break
    # 체킹
    checking()
print(cnt)