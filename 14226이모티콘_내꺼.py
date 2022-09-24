import sys
input = sys.stdin.readline
from collections import deque




S = int(input())
screen = 1
board = 1
queue = deque()
time = [0]*1001
# 영선이는 효빈이에게 이모티콘 S개를 보낸다.

# 각 연산은 1초씩 소모.
# 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 화면에 있는 이모티콘 중 하나를 삭제한다.

# 최초 1개 -> s개를 만드는데 연산은 저장 붙혀넣기 2초에 2배. or 1초에 클립보드 만큼 가져올 수 있음. 1초에 -1
# 
# 
# 핵심 아이디어는 time을 2차원배열 time[screen][board]형태로 만들어야 겹치는 값이 안들어감. 
# 변하는 변수가 2개여서 쌍으로 움직여야하고 1차원 dp가 값이 중복해서 들어간다? => 2차원 dp로 변경.
queue.append([screen,board])
while queue:
    screen,board = queue.popleft()
    if screen == S:
        print(time[S])
        break
    for next in (screen-1,screen,screen+board):
        if 0<=next < 1001 and not time[next]:
            if next == screen:
                board = screen
            queue.append([next,board])
            time[next] = time[screen] + 1


