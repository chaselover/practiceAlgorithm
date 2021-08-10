import sys
input = sys.stdin.readline
from collections import deque
from math import floor

def search_unions(x,y):
    queue = deque()
    nation_cnt=1
    sum_population = maps[x][y]
    queue.append([x,y])
    finish_union[x][y] = union_num
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and finish_union[nx][ny]==-1 and L<=abs(maps[x][y] - maps[nx][ny])<=R:
                nation_cnt+=1
                sum_population += maps[nx][ny]
                finish_union[nx][ny] = union_num
                queue.append([nx,ny])
    average_population = floor(sum_population/nation_cnt)
    return average_population

N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

cycle = 0
while True:
    unions = []
    # 전 국토에서 국경선이 열리는 연합국가 조사.(인접 L이상 R이하)
    finish_union = [[-1 for _ in range(N)] for _ in range(N)]
    union_num=0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<N and 0<=ny<N and finish_union[nx][ny]==-1 and L<=abs(maps[i][j] - maps[nx][ny])<=R:
                    unions.append(search_unions(i,j))
                    union_num+=1
    # 언제 종료할껀데? -> 조사했을 시 연합국가가 하나도 없을 시.
    if not unions:
        break

    # 한 사이클 동안 모든 연합국가에 대해 평균값 부여(소숫점 버림.)
    for k in range(len(unions)):
        for i in range(N):
            for j in range(N):
                if finish_union[i][j]==k:
                    maps[i][j] = unions[k]
    cycle += 1
print(cycle)