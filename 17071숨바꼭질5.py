import sys
input = sys.stdin.readline
from collections import deque

def BFS(N,K):
    odd_even_visited = [[False]*500001 for _ in range(2)]
    queue = deque()
    queue.append([N,K,0,0])
    cur_sister = K
    odd_even_visited[0][N] = True
    while queue:
        cur_node,cur_sister,cur_time,cur_flag = queue.popleft()
        if cur_sister > 500000:
            print(-1)
            exit()
        # 중복 체크가 불가능한 BFS(target이 움직여서 방문한곳 또 들러야함)는 순환구간을 찾아 check하면 됨.
        #  +1, -1 구간에 동생이 오면 걸림.
        if odd_even_visited[cur_flag][cur_sister]:
            print(cur_time)
            exit()
        new_flag = cur_flag^ 1
        for next_node in (cur_node-1,cur_node+1,cur_node*2):
            if 0<=next_node<=500000 and not odd_even_visited[new_flag][next_node]:
                next_time = cur_time + 1
                next_sister = cur_sister + next_time
                odd_even_visited[new_flag][next_node] = True
                queue.append([next_node,next_sister,next_time,new_flag])
                

N,K = map(int,input().split())
BFS(N,K)
