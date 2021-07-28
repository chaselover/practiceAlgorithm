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
# que에 넣는 것은 검사해야하는 수열의 숫자.
for num in seqs:
    # que에 있는 숫자의 다음에 와야하는 숫자를 가져와 
    # seqs의 num과 비교해 일치하면 que에 넣고 
    # 일치하지 않으면 idx를 늘려서 que의 다음 숫자가 num을 포함하는지 검사하는 방식.
    # idx가 큐의 마지막까지 왔는데 num이 큐에 있는 숫자의 다음숫자(tree집합)에 포함되지 못했다면
    # BFS에 따르지 않았다는 뜻. 아래 반복문은 온전히 BFS의 큐 삽입 순서에 따라 작동함.
    # num이 큐 내부에 있는(이미 BFS검사가 끝난) 노드의 tree에 있다면 큐에 넣고 아니면 큐 내부의 다른 숫자를 검사하는 방식.
    # 큐 내부에서 num으로 이어지는 방법이 없다면 BFS가 될 수 없는 수열이라는게 증명.
    while num not in tree[que[idx]]:
        idx+=1
        if idx == len(que):
            print(0)
            exit()
    que.append(num)
print(1)