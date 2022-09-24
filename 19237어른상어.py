import sys
input = sys.stdin.readline

# 상어 1~M까지 번호
# 상어들은 냄새를 뿌린다 / 1초마다 사방중 하나로 이동한다. / 냄새는 상어가 k번 이동하고 사라진다.
# 이동방향은 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡고 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
# 자신의 냄새가 여러개일 경우 특정 우선순위를 기준으로 방향을 잡는다.
# 상어가 이동한 후 한칸에 여러마리 상어가 있으면 가장 작은 번호 상어만 살아남고 나머지는 사라진다.
N,M,K = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
init_dir = list(map(int,input().split()))
priority_dir = {i:[list(map(int,input().split())) for _ in range(4)] for i in range(1,M+1)}
status_map = [[[0,0] for _ in range(N)] for _ in range(N)]
# 상어의 초기 상태값
shark_status = {}
for i in range(N):
    for j in range(N):
        if maps[i][j]:
            shark_status[maps[i][j]] = [i,j,init_dir[maps[i][j]-1]]
            status_map[i][j][0] = maps[i][j]
            status_map[i][j][1] = K

dx = [0,-1,1,0]
dy = [1,0,0,-1]
# 상어를 1번부터 순서대로 움직여야하고 이미 그 위치에 다른 상어가 있다면 사망.
shark_cnt = M
time=1
while shark_cnt !=1: # 상어 한마리 될때까지 조사.
    if time>1000:
        print(-1)
        exit()
    for shark in range(1,M+1):
        x,y,dir = shark_status[shark]
        if maps[x][y] == shark: # 상어 살아있으면 조사.
            dir_set = priority_dir[shark][dir-1]
            for next_dir in dir_set:
                next_x = x + dx[next_dir%4]
                next_y = y + dy[next_dir%4]
                if 0<=next_x<N and 0<=next_y<N:
                    if maps[next_x][next_y]: # 상어있으면 죽음
                        maps[x][y] = 0
                        shark_cnt -= 1
                        break
                    else:
                        if status_map[next_x][next_y][1]<time: # 피냄새 지속시간 지났으면 들어가.
                            shark_status[shark] = [next_x,next_y,next_dir]
                            maps[next_x][next_y] = shark
                            status_map[next_x][next_y][0] = shark
                            status_map[next_x][next_y][1] = time+K
                            break
                        else: # 못들어가면 다음 우선순위 방향으로 탐색
                            continue
            else: # 4방향 전부 불가능하면 내 냄새가 왔던곳으로 나감.
                for next_dir in dir_set:
                    next_x = x + dx[next_dir%4]
                    next_y = y + dy[next_dir%4]
                    if 0<=next_x<N and 0<=next_y<N:
                        if maps[next_x][next_y]:
                            maps[x][y] = 0
                            shark_cnt -= 1
                        if status_map[next_x][next_y][0]==shark:
                            shark_status[shark] = [next_x,next_y,next_x]
                            maps[next_x][next_y] = shark
                            status_map[next_x][next_y][0] = shark
                            status_map[next_x][next_y][1] = time+K
                            if maps[x][y] == shark:
                                maps[x][y] = 0
                            break
        else:
            continue
    time+=1
print(time)