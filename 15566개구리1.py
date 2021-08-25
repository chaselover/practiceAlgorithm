import sys
input = sys.stdin.readline


def DFS(depth,flogs):
    if depth==N:
        print('YES')
        print(*flogs)
        exit()
    for leaf in range(1,N+1):
        if not visited_leaf[leaf]:  # 배치 안된 잎
            for flog in range(1,N+1):
                if not choosed_flog[flog]:  # 배치 안된 개구리
                    if leaf in favor_leaf[flog]:     # 선호하는 연꽃에 배치.
                        # 연결된 통나무 반대편 노드 검사. 통나무 번호의 c값에 대해 양 개구리의 선호도가 일치하는지 확인.
                        for next_leaf,topic in graph[leaf]:
                            if visited_leaf[next_leaf] and frog_favor_topic[flog][topic] != frog_favor_topic[visited_leaf[next_leaf]][topic]:
                                return
                            visited_leaf[leaf] = flog
                            choosed_flog[flog] = True
                            DFS(depth+1,flogs+[flog])
                            visited_leaf[leaf] = 0
                            choosed_flog[flog] = False
                            

N, M = map(int, input().split())
frog_favor_topic = {i: [0] + list(map(int, input().split())) for i in range(1,N+1)}
favor_leaf = {i: list(map(int,input().split())) for i in range(1, N+1)}
graph = {i:[] for i in range(1, N+1)}
visited_leaf = {i: 0 for i in range(1,N+1)}
choosed_flog = {i: False for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


DFS(0,[])
print('NO')