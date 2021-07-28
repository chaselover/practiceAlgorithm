# 정점 1~N,양방향 그래프
# 1. 큐에 시작정점을 넣는다. 시작은 1이다 1을 방문했다고 처리한다.
# 2. 큐가 비어있지 않은동안 반복. 큐꺼내서 x 방문하지 않은 연결된 정점 y를 큐에 어팬드.
import sys
input = sys.stdin.readline

N = int(input())
tree = {i:[] for i in range(1,N+1)}
tree[0] = [1]

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a] += [b]
    tree[b] += [a]

seqs = list(map(int,input().split()))
que=[0]
idx=0
for num in seqs:
    while num not in tree[que[idx]]:
        idx+=1
        if idx == len(que):
            print(0)
            exit()
    que.append(num)
print(1)