import sys
input = sys.stdin.readline
from collections import deque

# 그냥 BFS로 위아래 움직이면 된다. 숨바꼭질문제보다 하위문제.
def BFS(F,S,G,U,D):
    dp_count = {i:float('inf') for i in range(1,F+1)}
    dp_count[S] = 0
    queue = deque()
    queue.append(S)
    while queue:
        cur_stair = queue.popleft()
        if cur_stair == G:
            print(dp_count[G])
            return
        for next_stair in (cur_stair+U,cur_stair-D):
            if 1<=next_stair<=F and dp_count[next_stair] > dp_count[cur_stair]+1:
                dp_count[next_stair] = dp_count[cur_stair]+1
                queue.append(next_stair)
    if dp_count[G]==float('inf'):
        print('use the stairs')

F,S,G,U,D = map(int,input().split())


BFS(F,S,G,U,D)