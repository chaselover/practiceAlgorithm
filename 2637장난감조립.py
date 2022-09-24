import sys
input = sys.stdin.readline
from collections import defaultdict,deque

def BFS():
    global dp_items
    dp_items = [[0]*(N+1) for _ in range(N+1)]              # level 0 부터 N번 부품까지 각 필요부품 갯수를 상향으로 쌓는다.
    queue = deque()
    for i in range(1,N+1):                                  # inititalize
        if level[i] ==0:
            queue.append(i)
    while queue:
        cur_item = queue.popleft()
        for next,next_items in subs[cur_item]:
            if sum(dp_items[cur_item])==0:                  #level=0인 애들은 dp[next]에 next조합에필요한 갯수만큼 적어준다.
                dp_items[next][cur_item] +=next_items
            else:                                           #전 부품 있는 애들은 전꺼 조합에 필요한 갯수*필요한 전꺼 갯수
                for i in range(1,N+1):
                    dp_items[next][i] += dp_items[cur_item][i] * next_items

            level[next] -=1                                 #계산 끝나면 level down으로 하층으로 보낸다.
            if level[next]==0:                              #더 이상 받는 부품이 없으면 queue에 넣어 그 윗층계산을 하게한다.
                queue.append(next)

N = int(input())
M = int(input())

subs = defaultdict(list)
level = [0]*(N+1)
for _ in range(M):                                      # 아래쪽 부터 올라갈 것이므로 화살표 방향도 Y->X로 가게끔 설계
    X,Y,K = map(int,input().split())
    subs[Y].append((X,K))
    level[X] +=1

BFS()

for i in range(1,N):            #N번 부품이 각각 필요한 재료를 index와 tuple로 packaging해 출력한다.
    cnt = dp_items[N][i]
    if cnt:                  
        print(i,cnt)