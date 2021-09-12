from collections import deque
from copy import deepcopy

def solution(board, aloc, bloc):
    # 각 플레이어 캐릭터 하나씩
    # 각 격자는 발판이 있거나 없거나
    # 이동 시 밟고 있던 발판은 사라짐.
    # 움직일 차례인데 상하좌우 못움직이면 해당 플레이어 패배.
    # 같은 발판인데 상대가 먼저 움직여 발판이 사라지면 패배
    # A먼저 시작. 최적의 플레이. 
    N = len(board)
    M = len(board[0])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    queue = deque()
    ax,ay = aloc
    bx,by = bloc
    if ax==bx and ay==by:
        return 0
    min_cnt = float('inf')
    queue.append([ax,ay,bx,by,board,0])
    while queue:
        ax,ay,bx,by,new_board,cnt = queue.popleft()
        tmp = deepcopy(new_board)
        flag_x = 0
        for i in range(4):
            nax = ax + dx[i]
            nay = ay + dy[i]
            if 0<=nax<N and 0<=nay<M and tmp[nax][nay]:
                tmp[ax][ay] = 0
                cnt += 1
                flag_x = 1
                flag_y = 0
                for i in range(4):
                    nbx = bx + dx[i]
                    nby = by + dy[i]
                    if 0<=nbx<N and 0<=nby<M and tmp[nbx][nby]:
                        cnt += 1
                        tmp[bx][by] = 0
                        queue.append([nax,nay,nbx,nby,tmp,cnt])
                        flag_y = 1
        if not flag_x or not flag_y:
            min_cnt = min(min_cnt,cnt)
    return min_cnt


print(solution([[1, 1, 1, 1, 1]],[0, 0],[0, 4]))