'''
설명은
https://blog.naver.com/na_qa/221531904546
'''
import sys
from collections import deque
input = lambda:sys.stdin.readline().strip()
INF = sys.maxsize

n = int(input())
graph = [[]for i in range(n+1)]
size = [INF for i in range(n+1)]
speed = [INF for i in range(n+1)]
intel = [INF for i in range(n+1)]
for i in range(1,n+1):
    size[i],speed[i],intel[i] = map(int, input().split())

#n개에 대해 전수조사
for i in range(1,n+1):
    for j in range(1,n+1):
        size_i, size_j,speed_i,speed_j,intel_i,intel_j = size[i],size[j],speed[i],speed[j],intel[i],intel[j]
        #만약 값이 모두 크거나 같다면
        if size_i>=size_j and speed_i>=speed_j and intel_i>=intel_j:
            #그런데 모두 같은 경우, i==j일수도 있고, 또한 2번 중복(i->j, j->i)되기때문에 i>j라는 조건을 걸어줌
            if size_i==size_j and speed_i==speed_j and intel_i==intel_j and i>=j:
                continue
            graph[i].append(j)


def bfs(): #그룹A의 Node들의 Level을 매기기 위해서
    que = deque()
    for a in range(1,n+1):
        if len(groupA[a])<2: #매칭되어있지않으면 level은 0으로 시작
            dist[a] = 0
            que.append(a)
        else:
            dist[a] = INF
    dist[0] = INF
    while que: #그룹A의 Node들의 Level을 측정
        a = que.popleft()
        if dist[a] < dist[0]:
            for b in graph[a]:
                if dist[groupB[b]] == INF:
                    dist[groupB[b]] = dist[a] + 1
                    que.append(groupB[b])
    return dist[0] != INF
def dfs(a):
    if a:
        for b in graph[a]: #그룹A의 a번째 Node와 연결되어있는 그룹B의 b중에서
            #(매칭되어있지않거나, b에 연결된 a'와 a의 Level이 1차이 나거나), (b에 연결되어있는 a'가 (매칭되어있지않거나, level이 1차이 나면))
            if dist[groupB[b]] == dist[a] + 1 and dfs(groupB[b]):
                groupA[a].append(b)
                groupB[b] = a
                return 1
        dist[a] = INF
        return 0
    return 1

groupA = [[] for i in range(n+1)]
groupB = [0 for i in range(n+1)]
dist = [INF for i in range(n+1)] #그룹A의 Node들의 Level
match = 0 #매칭숫자
while bfs():
    for a in range(1, n+1):
        if len(groupA[a])<2: #매칭이 안되어있고
            match += dfs(a)
        if len(groupA[a])<2:
            match += dfs(a)
print(n-match)