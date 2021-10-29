import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappop, heappush


def move_fish(arr):
    ret = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while arr[x][y]:
                d = arr[x][y].pop()
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + delta[i][0], y + delta[i][1]
                    if (nx, ny) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        ret[nx][ny].append(i)
                        break
                else:
                    ret[x][y].append(d)
    return ret


def move_shark(s):
    x, y = s
    q = deque()
    # 현재좌표, 방문좌표, 방향점수, 총갯수, 
    q.append((x, y, set(), '', 0))
    for _ in range(3):
        for _ in range(len(q)):
            x, y, visited, dir_score, cnt = q.popleft()
            for i in range(1, 5):
                nx, ny = x + s_delta[i][0], y + s_delta[i][1]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if (nx, ny) in visited:
                        q.append((nx, ny, visited, dir_score + str(i), cnt))
                    else:
                        q.append((nx, ny, visited | {(nx, ny)}, dir_score + str(i), cnt + len(tmp[nx][ny])))
    heap = []
    while q:
        x, y, visited, dir_score, cnt = q.pop()
        heappush(heap, (-cnt, int(dir_score), x, y, visited))
    cnt, score, x, y, visited = heappop(heap)
    for i, j in visited:
        if tmp[i][j]:
            tmp[i][j].clear()
            smell[i][j] = 3
    return (x, y)


M, S = map(int, input().split())
fishes = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
s_delta = [0, (-1, 0), (0, -1), (1, 0), (0, 1)]
matrix = [[[] for _ in range(4)] for _ in range(4)]
for x, y, d in fishes:
    matrix[x][y].append(d)
    
shark = tuple(map(lambda x: int(x) - 1, input().split()))
smell = [[0] * 4 for _ in range(4)]
for _ in range(S):
    # 모든 물고기 정보 복제 tmp. 5번에서 더해줌.
    tmp = [[k[:] for k in row] for row in matrix]
    # 모든 물고기 한칸 이동. 물고기 냄새 있거나 상어있으면 이동 불가. 이동할 수 있을때까지 delta -1 없으면 이동불가.
    tmp = move_fish(tmp)
    # 상어 연속 3칸 이동. 상하좌우로 인접한 칸으로 이동할 수 있다. 범위를 벗어나면 불가능한 이동.
    shark = move_shark(shark)
    # 이동 중에 상어가 물고기 있는  칸으로 이동하면 그 칸의 모든 물고기는 삭제. 냄새를 남김. 가능한 방법 중 물고기가 가장 많은 바법으로 남김.
    # 여러가지인경우 사전순으로 이동. 상은 1, 좌는 2, 하는 3, 우는 4. 사전순 앞서는 경우로 이동.
    # 2턴 전 냄새 사라짐.
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
    # 물고기 배열 tmp fishes에 더해줌.
    for i in range(4):
        for j in range(4):
            matrix[i][j] += tmp[i][j]
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(matrix[i][j])

print(answer)