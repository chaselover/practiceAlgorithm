import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]
princess = deque()
ans = set()
A = [[] for _ in range(5)]
visit = [[False] * 5 for _ in range(5)]

def go(n, cnt):
    if (cnt + (7 - n) < 4):
        return

    if n == 7:
        if cnt >= 4:
            temp = list(princess)
            temp.sort()
            temp = tuple(temp)
            ans.add(temp)
        return

    possible = set()
    for node in princess:
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if nx < 0 or ny < 0 or nx == 5 or ny == 5 or visit[nx][ny]:
                continue

            possible.add((nx,ny))

    for node in possible:

        visit[node[0]][node[1]] = True
        princess.append(node)
        if A[node[0]][node[1]] == 'S':
            go(n+1, cnt+1)
        else:
            go(n+1, cnt)
        princess.pop();
        visit[node[0]][node[1]] = False

for i in range(5):
    A[i] = list(input().rstrip())

for i in range(5):
    for j in range(5):
        if A[i][j] == 'S':
            visit[i][j] = True
            princess.append((i,j))
            go(1,1)
            princess.popleft()

print(len(ans))