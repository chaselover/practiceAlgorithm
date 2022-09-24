from collections import deque
import sys
def bfs(q, cnt = 0):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while q:
        cnt += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= N or nx < 0 or ny >= M or ny < 0 or arr[nx][ny] != 0:
                    continue
                arr[nx][ny] = 1
                q.append((nx,ny))
    if check(arr):
        return cnt - 1
    else:
        return -1

def check(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return False
                break
    return 1

if __name__ == "__main__":
    input = sys.stdin.readline
    M, N = map(int,input().split())
    q = deque([])
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i,j))
    print(bfs(q))