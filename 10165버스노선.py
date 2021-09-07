import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
path1 = []
path2 = []
visited = {i: False for i in range(1,M+1)}
minA = int(1e12)
maxB = -1
# 0을 거치는 최장 범위 minA ~ maxB를 구하고 모든 간선을 0을 거치는 것과 그렇지 않은것으로 나눔.
for i in range(1,M+1):
    a, b = map(int, input().split())

    if a <= b:
        path1.append((a,b,i))
    else:
        minA = min(minA, a)
        maxB = max(maxB, b)
        b = b + N
        path2.append((a,b,i))
    visited[i] = True
# 모든 간선을 시작점 오름차순, 종료지점 내림차순으로 정리.(종료지점이 길어야 뒤에애들은 다 탈락.)
path1.sort(key=lambda x : (x[0],-x[1]))
path2.sort(key=lambda x : (x[0],-x[1]))

right = 0
for i in range(len(path1)):
    # 0을 거치지 않는 노선의 시작점과 종료점이 영역 안으로 들어온 path면 삭제시킴.(라인 스위핑)
    if minA <= path1[i][0]:
        visited[path1[i][2]] = False
    if maxB >= path1[i][1]:
        visited[path1[i][2]] = False
    # 마찬가지로 right 안쪽이면 다 삭제.
    if path1[i][1] <= right:
        visited[path1[i][2]] = False
    # 포함 안됐으면 간선 추가시킴.
    else:
        right = path1[i][1]

# 0거쳐가는애들도 오른쪽 끝이랑 0이랑 비교해서 점점 범위 늘려나감(시작점, 끝점.)
right = 0
for i in range(len(path2)):
    if path2[i][1] <= right:
        visited[path2[i][2]] = False
    else:
        right = path2[i][1]
    
for i in range(1,M+1):
    if visited[i]:
        print(i,end=' ')