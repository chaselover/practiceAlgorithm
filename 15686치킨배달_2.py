import sys
input = sys.stdin.readline

from itertools import combinations

# 맵크기(N), 치킨집 최대 선택가능개수(M)
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 빈칸(0), 집(1), 치킨집(2) // 그래프 그리기.
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1: 
            house.append((i, j))
        elif board[i][j] == 2: 
            chicken.append((i, j))

# 모든 치킨집 조합에 대해 
minv = float('inf')
for ch in combinations(chicken, M):
    sumv = 0
    # 모든 집들에 대해 치킨집 조합에 속한 치킨집들에 대한 거리의 합이 최솟값보다 작으면 최신화.(거리값은 x좌표 차이 절댓값 + y좌표차이 절댓값.)
    # min에 들어가는 인자수는 치킨집 수만큼 돌아가고 그중 각 집집마다 최솟값만 골라서 sum에 합산.
    for home in house:
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        if minv <= sumv: 
            break
    if sumv < minv: 
        minv = sumv

print(minv)

