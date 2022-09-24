from collections import deque

# 어차피 time(move)배열에 전에 어떤 숫자에서 이동 했는지 다 기록해놨음.
# 즉경로같이 이전에 어디서 왔나 알아야 하는 것들은 전부 dp처럼 기록해서 처리.
# answer arr에 목적지부터 이동한 time횟수만큼 dp역추적해서 지나간 path전부 저장 후 역순으로 프린트.
def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x+1, x-1, 2*x):
            if 0<=i<=100000 and dist[i]==0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, input().split())
dist = [0]*100001
move = [0]*100001
bfs()