import sys 
input = sys.stdin.readline 
from collections import deque 

N, K = map(int, input().split()) 
conveier = deque()
conveier.extend(list(map(int, input().split())))
robot = deque()
robot.extend([0]*N)
K_cnt = conveier.count(0)
ans=0
while K_cnt <K:
    # conveier,robot한칸씩 회전
    conveier.rotate(1)
    robot.rotate(1)
    robot[-1]=0
    # 로봇이 한칸 이동할 수 있으면 이동한다.
    for i in range(N-2,-1,-1):
        if robot[i] and not robot[i+1] and conveier[i+1]:
            robot[i+1] = 1
            robot[i] = 0
            conveier[i+1] -= 1
            if not conveier[i+1]:
                K_cnt+=1
    # 내리는위치 로봇은 내린다.
    robot[-1] = 0
    # 올리는 위치에 있는 칸이 내구도가 0이 아니면 로봇 올린다.
    if conveier[0]:
        robot[0]=1
        conveier[0]-=1
        if not conveier[0]:
            K_cnt+=1
    ans+=1
print(ans)