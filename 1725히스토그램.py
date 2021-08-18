import sys
input=sys.stdin.readline


n=int(input())
graph=[]
result=0
left=0
a=0
for _ in range(n):
    graph.append(int(input()))
graph.append(0)
stack=[(0,graph[0])]
# cursor는 오른쪽으로 탐색할수록 커짐. stack에 cursor위치와 그곳의 높이를 집어넣음.
# stack의 제일 위층 의 높이(전층의 높이)가 이번 층의 높이보다 크면 즉 이번 층이 작으면
# stack에서 한칸씩 왼쪽으로 돌아가면서 면적 측정. 면적 = 빠진사각형 높이*(내위치-그 사각형 위치)
# 나보다 낮은 곳까지 stack을 pop하면서 계산한 후 다시 내위치부터 append하며 오른쪽으로 진행.
# stack에 남아있는 애들은 후에 걔들보다 낮은 위치의 사각형이 나오면 그때 pop하며 마저 계산해줌.
for now in range(1,n+1):
    left=now
    while stack and stack[-1][1]>graph[now]:
        left,temp=stack.pop()
        result=max(result,temp*(now-left))
    stack.append((left,graph[now]))

print(result)