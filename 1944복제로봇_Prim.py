import sys
input = sys.stdin.readline
from collections import deque


# S부터 각 K까지 거리, K에서 각 K까지 거리 탐색을 위한 BFS, 각 K자리에 cnt값 기록.
def BFS(x,y,graph,start,key):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    check = [[False]*N for _ in range(N)]
    queue = deque()
    queue.append([x,y])
    check[x][y] = True

    # reps는 바퀴수(거리)
    # 즉 graph에 node번호 e와 가중치 reps를 넣어줌.
    reps = 1
    while queue:
        for _ in range(len(queue)):
            vx,vy = queue.popleft()
            for i in range(4):
                nx = vx+dx[i]
                ny = vy+dy[i]
                if 0<=nx<N and 0<=nx<N and not check[nx][ny]:
                    if maze[nx][ny] >= 2:
                        e = maze[nx][ny]
                        if graph.get(start):                     # graph에 start시작점 정점번호, 가중치 있으면 가져와서 하나 더 넣어줌.
                            graph.get(start).append((e,reps))   #  즉 start라는 key에 정점정보가 계속 담김.
                        else:
                            graph[start] = [(e,reps)]           # graph에 start시작점 정점번호, 가중치 없으면 선언해줌.
                        queue.append((nx,ny))
                        key -= 1                                # key찾을때마다 하나씩 -해서 다 끝났을 떄 key가 남아있으면 false
                    elif maze[nx][ny] ==0:
                        queue.append((nx,ny))
                    check[nx][ny]=True
        reps +=1
    if key:
        return False
    else:
        return True


def prim(graph,start,M):
    minWeight = [float('inf')] * (M+3)                           # 최초 가중치 전부 무한대로 key갯수+시작지점 (idx 2부터 시작했으므로 2칸 더 더해줌.)
    visited = [0] * (M+3)                                       
    minWeight[0] = minWeight[1] = minWeight[start] = 0           # 그냥 준 0,1 idx 요소 0으로 초기화, start요소 0으로 시작.

    for _ in range(2,M+3):                                      # 2번 노드부터 M+2번 노드까지 key+S의 갯수만큼 반복
        minidx, minval = 0,float('inf')                         
        for j in range(2,M+3):                                 
            if not visited[j] and minWeight[j] < minval:        # j노드에 방문 안했고, j의 최소 가중치가 최소값(연결된 모든 가중치 중의 촤솟값)보다 작으면 (즉 최초 0과 이어져 있는 노드들만)
                minval = minWeight[j]                           # j의 minWeight는 minval(가중치의 값이 가장 작은 것(최솟값을 찾기위함))
                minidx = j                                      # j는 최솟값을 가진 연결된 노드임을 표시
        visited[minidx] = 1                                     # 최소 가중치를 가진 minidx로 방문.
        for e,val in graph.get(minidx):                         # graph에서 가장 작은 idx의 node번호, 가중치 값을 가져온다.
            if not visited[e] and minWeight[e] > val:           # 방문안했고 가중치값보다 minWeight에 기록된 가중치가 더 크면
                minWeight[e] = val                              # 최소가중치값에 가중치값을 저장해준다.
                                                                # 위과정을 M+1번 반복한다.(M+1개의 노드를 잇기위해서.)
    
    return sum(minWeight)                                       # MST의 가중치값 합을 리턴한다.



N,M = map(int,input().split())
maze = [list(map(str,input().rstrip())) for _ in range(N)]


# maze에서 S,K찾기 / S,K는 0,1로부터 구분하기 위해 2부터 시작.
points = []
idx = 2
start = 0
for i in range(N):
    for j in range(N):
        if maze[i][j] == 'S' or maze[i][j] == 'K':
            if maze[i][j] == 'S':
                start = idx                             # start에서 시작하기 위해 'S'를 찾으면 그 idx를 start에 저장함.
            maze[i][j] = idx
            idx += 1
            points.append([i,j])
        else:
            maze[i][j] = int(maze[i][j])
            
graph = dict()
for i in range(N):
    for j in range(N):
        if maze[i][j] >=2:
            if not BFS(i,j,graph,maze[i][j],M):     # 모든 열쇠 탐색 불가능 하면 -1출력.
                print(-1)
                exit()

print(prim(graph, start,M))



