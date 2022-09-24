import sys
from collections import deque
input = sys.stdin.readline


def find_baby_shark(N, matrix):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 9:
                matrix[i][j] = 0
                baby_shark = (i,j,2,0)
    return baby_shark


def find_feed(N, matrix, size):
    feeds = []
    for i in range(N):
        for j in range(N):
            if 0 < matrix[i][j] < size:
                feeds.append([i,j])
    return feeds


def find_target(x, y, arr):
    min_dist = 41
    for feed in arr:
        dist = abs(feed[0] - x) + abs(feed[1] - y)
        if dist < min_dist:
            min_dist = dist
            target_x, target_y = feed[0], feed[1]
    return target_x, target_y


def BFS(x, y, target_x, target_y, size):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 0
    eat_feed = []
    while queue:
        x,y = queue.popleft()
        if x==target_x and y==target_y:
            eat_feed.append([x,y,visited[x][y]])
            return eat_feed
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 나보다 크기가 큰 물고기가 있는 칸은 못지나감.
            if 0 <= nx < N  and 0 <= ny < N and visited[nx][ny]==-1:
                if matrix[nx][ny] <= size:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
                if 0 < matrix[nx][ny] < size:
                    eat_feed.append([nx,ny,visited[nx][ny]])

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
time = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

x, y, size, eat_cnt = find_baby_shark(N, matrix)

# 상태공간 돌며 나보다 크기가 작은게 있으면 순회 종료. BFS시작. 찾아서 잡아먹음. 거리 차이만큼 시간 증가.
while True:
    feed_box = find_feed(N, matrix, size)
    if feed_box:
        target_x, target_y = find_target(x, y, feed_box)
        arr = BFS(x, y, target_x, target_y, size)
        if arr:
            arr.sort(key = lambda x: (x[2], x[0],x[1]))
            x, y,plus_time = arr[0][0],arr[0][1],arr[0][2]
            matrix[x][y] = 0
            time += plus_time
            eat_cnt += 1
            if eat_cnt == size:      # 먹은 갯수가 내 크기랑 같아지면 크기 업 먹은갯수 초기화
                size += 1
                eat_cnt = 0
    else:               # 다 돌았는데 작은거 없으면 탐색 종료
        print(time)
        exit()


