import sys
input = sys.stdin.readline
from collections import deque

def spring_summer():
    for i in range(n):
        for j in range(n):
            len_t = len(tree_map[i][j])
            for k in range(len_t):
                if tree_map[i][j][k] <= area[i][j]:
                    area[i][j] -= tree_map[i][j][k]
                    tree_map[i][j][k] += 1
                else:
                    for _ in range(len_t-k):
                        area[i][j] += tree_map[i][j].pop() // 2
                    break
def fall_winter():
    for i in range(n):
        for j in range(n):
            for k in tree_map[i][j]:
                if k % 5:
                    continue
                for l in range(8):
                    x = i + dx[l]
                    y = j + dy[l]
                    if 0 <= x < n and 0 <= y < n:
                        tree_map[x][y].appendleft(1)
            area[i][j] += energy[i][j]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
n, m, k = map(int, input().split())
energy = [list(map(int, input().split())) for _ in range(n)]
tree_map = [[deque() for _ in range(n)] for _ in range(n)]
area = [[5] * n for _ in range(n)]
for i in range(m):
    x, y, z = map(int, input().split())
    tree_map[x - 1][y - 1].append(z)
for i in range(k):
    spring_summer()
    fall_winter()
answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree_map[i][j])
print(answer)




###다른사람
import sys
input = sys.stdin.readline


def solve():
    n, m, k = map(int, input().split())
    land = [[5]*n for _ in range(n)]
    tree = [[{} for _ in range(n)] for _ in range(n)]
    S2D2 = [list(map(int, input().split())) for _ in range(n)]
    for _ in range(m):
        r, c, a = map(int, input().split())
        tree[r-1][c-1][a] = 1
    for _ in range(k):
        ng = [[{} for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if not tree[r][c]:
                    land[r][c] += S2D2[r][c]
                    continue
                tmp = more = 0
                for age, count in sorted(tree[r][c].items()):
                    if (can := min(land[r][c]//age, count)):
                        land[r][c] -= age*can
                        if (nxt := age+1) not in ng[r][c]:
                            ng[r][c][nxt] = 0
                        ng[r][c][nxt] += can
                        if nxt % 5 == 0:
                            tmp += can
                    more += (age >> 1)*(count-can)
                land[r][c] += more + S2D2[r][c]
                if tmp:
                    if r > 0:
                        ng[r-1][c][1] = ng[r-1][c].get(1, 0) + tmp
                        if c > 0:
                            ng[r-1][c-1][1] = ng[r-1][c-1].get(1, 0)+tmp
                        if c < n-1:
                            ng[r-1][c+1][1] = ng[r-1][c+1].get(1, 0)+tmp
                    if r < n-1:
                        ng[r+1][c][1] = ng[r+1][c].get(1, 0)+tmp
                        if c > 0:
                            ng[r+1][c-1][1] = ng[r+1][c-1].get(1, 0)+tmp
                        if c < n-1:
                            ng[r+1][c+1][1] = ng[r+1][c+1].get(1, 0)+tmp
                    if c > 0:
                        ng[r][c-1][1] = ng[r][c-1].get(1, 0)+tmp
                    if c < n-1:
                        ng[r][c+1][1] = ng[r][c+1].get(1, 0)+tmp
        tree = ng
    print(sum(sum(tree[i//n][i % n].values()) for i in range(n**2)))


if __name__ == '__main__':
    solve()