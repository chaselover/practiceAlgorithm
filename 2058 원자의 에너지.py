import sys
input = sys.stdin.readline

def dfs(cur_node):
    visited[cur_node] = True
    for i in plus:
        if visited[cur_node+i]:
            continue



N, M = map(int, input().split())
atom_e ={int(input()): True for _ in range(N)}
plus = [int(input()) for _ in range(M)]
# 각 atom_e상태가 plus를 받아들이거나 빼서 다른 atom_e에 도달할 수 있다면 안됨. 즉 인접해있으면 안됨.-> 트리dp
# 어떤 atom_e의 조합을 선택해야 합이 최대가 되는가?

dfs(1)