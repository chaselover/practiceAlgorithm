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
# 상어의 초기 상태값
shark = {}
for i in range(N):
    for j in range(N):
        if maps[i][j]:
            shark[maps[i][j]] = [i,j,init_dir[init_dir[i][j]-1]]
# 이동상태를 저장할 3차원 배열
status_map = [[[0,0] for _ in range(N)] for _ in range(N)]

# 상어를 1번부터 순서대로 움직여야하고 이미 그 위치에 다른 상어가 있다면 사망.