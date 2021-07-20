from collections import deque 
import sys 
input = sys.stdin.readline

visited = [] 
result = 0 

def bfs(x, y, h): 
    global result
    dx = [-1, 0, 0, 1] 
    dy = [0, -1, 1, 0]
    queue = deque([(x, y)]) 
    out_flag = True 
    visited[x][y] = 1 
    cnt = 1                                 #1인것들 카운트 센다.
    while True: 
        x, y = queue.popleft() 
        for i in range(4): 
            rx = x + dx[i] 
            ry = y + dy[i]                  #바깥쪽이랑 연결된 부분은 버린다.(물 못담음)
            if rx == -1 or rx == N or ry == -1 or ry == M: 
                out_flag = False 
                continue 
            if board[rx][ry] <= h and visited[rx][ry] == 0: 
                visited[rx][ry] = 1 
                queue.append((rx, ry)) 
                cnt += 1 
        if not queue: 
            if out_flag: 
                result += cnt 
            return 

N, M = map(int, input().split()) 
board = [list(map(int, list(input().rstrip()))) for _ in range(N)] 

# 우리는 밑에서부터 한칸씩 채운다. 1~8높이까지.
for height in range(1, 9): 
    visited = [[0] * M for _ in range(N)] 
    # 중간에 고립된 부분들이 있으므로 모든 칸에서 다 bfs를 돌려본다.
    for i in range(N): 
        for j in range(M): 
            if board[i][j] <= height and visited[i][j] == 0: 
                bfs(i, j, height) 
print(result) 
