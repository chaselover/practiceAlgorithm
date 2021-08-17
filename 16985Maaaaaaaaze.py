import sys
input = sys.stdin.readline

# 1. 층 섞기(순열로 모든 경우의 수)
# 2. 층 회전 시키기.
# 3. 층을 순서대로 회전시킨 후 (0,0,0)칸과 (4,4,4)칸이 이동 가능한 칸인지 확인하고 BFS를 시작한다.
# 최단거리가 12이면 바로 종료한다. 
from itertools import permutations as perm
from collections import deque
from copy import deepcopy

def bfs(z, y, x):
    if maze[z][y][x] == 0:
        return -1
    queue = deque()
    queue.append((z, y, x))
    dist = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
    dist[z][y][x] = 0

    while queue:
        curr_z, curr_y, curr_x = queue.popleft()
        for d in direction:
            next_z = curr_z + d[0]
            next_y = curr_y + d[1]
            next_x = curr_x + d[2]
            if 0<=next_z<5 and 0<=next_y<5 and 0<=next_x<5:
                if maze[next_z][next_y][next_x] == 1 and dist[next_z][next_y][next_x] == -1:
                    dist[next_z][next_y][next_x] = dist[curr_z][curr_y][curr_x] + 1
                    queue.append((next_z, next_y, next_x))
    return dist[4][4][4]

def clockwise(a): # 회전
    tmp = a[0][:]
    a[0][:] = a[4][0], a[3][0], a[2][0], a[1][0], a[0][0]
    a[4][0], a[3][0], a[2][0], a[1][0], a[0][0] = a[4][4::-1]
    a[4][4::-1] = a[0][4], a[1][4], a[2][4], a[3][4], a[4][4]
    a[0][4], a[1][4], a[2][4], a[3][4], a[4][4] = tmp

    tmp = a[1][1:4]
    a[1][1:4] = a[3][1], a[2][1], a[1][1]
    a[3][1], a[2][1], a[1][1] = a[3][3:0:-1]
    a[3][3:0:-1] = a[1][3], a[2][3], a[3][3]
    a[1][3], a[2][3], a[3][3] = tmp

MAZE = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
direction = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))
block_perm = list(perm(list(range(5)))) # 순열 생성.
answer = -1

while block_perm:
    bp = block_perm.pop(0)

    maze = []
    for b in bp:
        maze.append(deepcopy(MAZE[b])) # 생성한 순열 순서대로 블럭을 쌓아준다.

    # 블럭을 밑에서부터 1번씩 회전시키면서 최단경로 탐색하기
    for _ in range(4):
        for _ in range(4):
            for _ in range(4):
                for _ in range(4):
                    for _ in range(4):
                        cnt = bfs(0,0,0)
                        if cnt != -1:
                            if answer == -1 or cnt < answer:
                                answer = cnt
                        clockwise(maze[4])
                    clockwise(maze[3])
                clockwise(maze[2])
            clockwise(maze[1])
        clockwise(maze[0])

print(answer)
