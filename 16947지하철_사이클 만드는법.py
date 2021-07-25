import sys
N=int(input())
parent=[0]*(N+1)
ans=[0]*(N+1)
graph=[[] for _ in range(N+1)]
graphSize=[0]*(N+1)

# 그래프 생성
for _ in range(N):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graphSize[a]+=1
    graphSize[b]+=1
    # 이사람은 graphSize라는 연결된 간선의 갯수를 측정해 size가 1인 놈.즉 가장 끝부분에 있는넘들을 삭제해가는 식으로 
    # 싸이클을 찾음. 애포에 사이클이 없으면 간선이 1인놈이 있을수밖에없음 그런놈들을 삭제.하면 간선이 2인 사이클들밖에 안남음.
    # 그래프사이즈 배열안에 1이 없을때까지 반복.

while 1 in graphSize:
    for i in range(1,N+1):
        if graphSize[i]==1:
            # 없애면서 노드i의 부모 노드를 기록해둠.
            parent[i]=graph[i][0]
            graphSize[i]=0
            graphSize[parent[i]]-=1
            graph[parent[i]].remove(i)
            
# 부모배열 (사이클 내에 있는 노드들)에대해 전부 검사. 한칸씩 
while any(parent):
    for i in range(1,N+1):
        # 부모노드가 있으면 들어가
        if parent[i]!=0:
            # 부모노드의 부모가 0이면
            if parent[parent[i]]==0:
                # 거리+1
                ans[i]=ans[parent[i]]+1
                parent[i]=0

for i in range(1,N+1):
    print(ans[i],end=' ')