import sys
input = sys.stdin.readline
from collections import deque

def make_electic(start,cur_cnt):
    queue = deque()
    dp[start] = 0
    answer=float('inf')
    if target_cnt==0 or cur_cnt>=target_cnt:
        return 0
    elif cur_cnt==0:
        return -1
    else:
        queue.append([start,0])
    while target_cnt > cur_cnt:
        # 한 순회에 하나씩 킬꺼임.
        circle_SIZE = len(queue)
        for _ in range(circle_SIZE):
            now,cost = queue.popleft()
            # 어떤 발전소 킬지 순회
            for i in range(N):
                if not now & (1<<i):
                    min_cost = float('inf')
                    for j in range(N):
                        # 발전소 켜져있으면 최솟값 찾아 갱신.
                        if now & (1<<j):
                            min_cost = min(min_cost,costs[j][i])
                    # i번째 발전소 최솟값으로 키는게 더싸면 킴
                    if dp[now|(1<<i)] > cost + min_cost:
                        dp[now|(1<<i)] = cost + min_cost
                        queue.append([now|(1<<i),cost + min_cost])
        cur_cnt+=1
    # cnt조건이 만족됐지만 최저값은 아직 큐안에 남아있을 수도 있으니 꺼내서 비교해줘야함.
    while queue:
        _,cost = queue.pop()
        answer = min(answer,cost)
    return answer

N = int(input())
costs = [list(map(int,input().split())) for _ in range(N)]
dp = [float('inf')]*(1<<N)
init_status = list(input())
start=0
cur_cnt=0
for i in range(N):
    if init_status[i]=="Y":
        start |= (1<<i)
        cur_cnt +=1

target_cnt = int(input())
print(make_electic(start,cur_cnt))