import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

def BFS(x,y,visited):
    queue = deque()
    visited[x][y] = True
    queue.append([x,y])
    kill_ai_stone = 1
    flag = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if baduk_board[nx][ny] == 0:
                    flag = 1
                elif baduk_board[nx][ny] == 2:
                    visited[nx][ny] = True
                    kill_ai_stone += 1
                    queue.append([nx,ny])
    return kill_ai_stone if not flag else -1


def play_game(put_stone):
    visited = [[False]*M for _ in range(N)]
    kill_count = 0
    for x,y in put_stone:
        baduk_board[x][y] = 1
    for i in range(N):
        for j in range(M):
            if baduk_board[i][j]==2 and not visited[i][j]:
                cnt = BFS(i,j,visited)
                if cnt != -1:
                    kill_count += cnt
    for x,y in put_stone:
        baduk_board[x][y] = 0
    return kill_count
    

N, M = map(int,input().split())
baduk_board = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]

pos = []
for i in range(N):
    row = list(map(int,input().split()))
    baduk_board.append(row)
    for j in range(M):
        num = row[j]
        if not num:
            pos.append((i,j))

max_kill_cnt = 0
for my_turn in combinations(pos,2):
    max_kill_cnt = max(max_kill_cnt,play_game(my_turn))
print(max_kill_cnt)