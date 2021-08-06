from copy import deepcopy
import sys
input = sys.stdin.readline
def fill(x, y, arr, dir):
    for i in dir:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 6:
                    break
                elif arr[nx][ny] == 0:
                    arr[nx][ny] = "#"
            else:
                break
def dfs(arr, cnt):
    global result
    temp = deepcopy(arr)
    if cnt == cctv_cnt:
        num = 0
        for i in range(n):
            num += temp[i].count(0)
        result = min(result, num)
        return
    x, y, cctv = cctvs_nums[cnt]
    # direction의 cctv안에있는 모든 방향성마다.dfs를 돌림.
    # fill로 칠하고 들어감. 나오면 temp arr로 초기화.
    for i in cctv_directions[cctv]:
        fill(x, y, temp, i)
        dfs(temp, cnt + 1)
        temp = deepcopy(arr)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cctv_directions = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[3, 0], [0, 2], [2, 1], [1, 3]], 
[[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]
n, m = map(int, input().split())
maps  = []
cctvs_nums = []
cctv_cnt = 0
result = 100000000
# 맵 그리면서
for i in range(n):
    a = list(map(int, input().split()))
    maps.append(a)
    for j in range(len(a)):
        if a[j] != 0 and a[j] != 6:
            cctvs_nums.append([i, j, a[j]])
            cctv_cnt += 1
dfs(maps, 0)
print(result)