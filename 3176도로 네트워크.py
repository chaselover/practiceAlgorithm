import sys
from collections import deque
from math import log2
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
logN = int(log2(N) + 1)
for _ in range(N-1):
    A, B, C = map(int, input().split())
    tree[A].append([B,C])
    tree[B].append([A,C])

#DFS
p_list = [[0,0] for _ in range(N+1)]
p_check = [True for _ in range(N+1)]
q = deque()
q.append(1)
p_check[1] = False
while q:
    a = q.popleft()
    for b,c in tree[a]:
        if p_check[b]:
            q.append(b)
            depth[b] = depth[a] + 1
            p_check[b] = False
            p_list[b][0] = a
            p_list[b][1] = c
# 아무 노드나 루트로 잡고 부모 저장

# 2^k 번째 부모노드와 가장 짧은 도로 가장 긴 도로 구하기
DP = [[[0,0,0] for _ in range(logN)] for _ in range(N+1)]
# 초기화
for i in range(N+1):
    DP[i][0][0] = p_list[i][0]
    DP[i][0][1] = p_list[i][1]
    DP[i][0][2] = p_list[i][1]

#희소 테이블 완성하기
for j in range(1,logN):
    for i in range(1,N+1):
        DP[i][j][0] = DP[DP[i][j-1][0]][j-1][0]
        DP[i][j][1] = min(DP[i][j-1][1],DP[DP[i][j-1][0]][j-1][1])
        DP[i][j][2] = max(DP[i][j-1][2],DP[DP[i][j-1][0]][j-1][2])

K = int(input())
for _ in range(K):
    D, E = map(int, input().split())
    if depth[D] < depth[E]:
        D,E=E,D
    dif = depth[D]-depth[E]
    shortest = float('inf')
    longest = 0
    # 레벨 맞추기
    for i in range(logN):
        if dif & 1 <<i:
            shortest = min(shortest,DP[D][i][1])
            longest = max(longest,DP[D][i][2])
            D = DP[D][i][0]
    
    if D==E:
        print(shortest,longest)
        continue

    # 최소 공통조상 찾기
    for i in range(logN-1,-1,-1):
        if DP[D][i][0] != DP[E][i][0]:
            shortest = min(shortest,DP[D][i][1],DP[E][i][1])
            longest = max(longest,DP[D][i][2],DP[E][i][2])
            D = DP[D][i][0]
            E = DP[E][i][0]
    
    shortest = min(shortest,DP[D][i][1],DP[E][i][1])
    longest = max(longest,DP[D][i][2],DP[E][i][2])
    print(shortest,longest)