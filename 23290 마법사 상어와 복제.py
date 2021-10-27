import sys
input = sys.stdin.readline


def move_fish(arr):
    ret = []
    for x, y, d in arr:
        for i in range(d, d - 8, -1):
            i %= 8
            nx, ny = x + delta[i], y + delta[i]
            if (nx, ny) != shark and not smell[nx][ny] and 0 <= nx < 4 and 0 <= ny < 4:
                ret.append((nx, ny, d))
                break
    return ret


def move_shark(s):
    x, y = s

M, S = map(int, input().split())
fishes = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
matrix = [[[] for _ in range(4)] for _ in range(4)]
for x, y, d in fishes:
    matrix[x][y].append(d)
    
shark = tuple(map(int, input().split()))
smell = [[0] * 4 for _ in range(4)]
for _ in range(S):
    # 모든 물고기 정보 복제 tmp. 5번에서 더해줌.
    tmp = fishes[:]
    # 모든 물고기 한칸 이동. 물고기 냄새 있거나 상어있으면 이동 불가. 이동할 수 있을때까지 delta -1 없으면 이동불가.
    tmp = move_fish(tmp)
    # 상어 연속 3칸 이동. 상하좌우로 인접한 칸으로 이동할 수 있다. 범위를 벗어나면 불가능한 이동.
    move_shark(skark)
    # 이동 중에 상어가 물고기 있는  칸으로 이동하면 그 칸의 모든 물고기는 삭제. 냄새를 남김. 가능한 방법 중 물고기가 가장 많은 바법으로 남김.
    # 여러가지인경우 사전순으로 이동. 상은 1, 좌는 2, 하는 3, 우는 4. 사전순 앞서는 경우로 이동.
    # 2턴 전 냄새 사라짐.
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
    # 물고기 배열 tmp fishes에 더해줌.
    fishes += tmp

