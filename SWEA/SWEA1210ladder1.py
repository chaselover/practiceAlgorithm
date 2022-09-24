import sys
sys.stdin = open('input.txt')
from collections import deque


def find_start(ladder):
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 2:
                return i, j


# 사다리게임을 합니다.
def do_ladder_game(ladder):
    visited = [[False for _ in range(100)] for _ in range(100)]
    init_x, init_y = find_start(ladder)     # 도착지를 찾습니다.

    dx = [0, 0, -1]
    dy = [1, -1, 0]

    queue = deque()
    queue.append([init_x, init_y])      # 도착지부터 역사다리 게임을 합니다.
    visited[init_x][init_y] = True
    while queue:
        x, y = queue.popleft()
        if not x:
            return y
        for i in range(3):              # 좌우를 먼저 살피고 못가면 위로갑니다.
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100 and not visited[nx][ny] and ladder[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append([nx, ny])
                break                   # 갔으면 다른 선택지로 분기가 나뉘는 것을 막습니다.


for _ in range(1, 11):
    test = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{test} {do_ladder_game(ladder)}')

