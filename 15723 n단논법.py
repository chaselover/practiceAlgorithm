import sys
input = sys.stdin.readline


def DFS(cur_node, target):
    if cur_node==target:
        return True
    for next_node in graph[cur_node]:
        if not visited[next_node]:
            visited[next_node] = True
            if DFS(next_node, target):
                return True


n = int(input())
graph = {i:[] for i in range(26)}
level = {i:0 for i in range(26)}
for _ in range(n):
    first, arrow, end = input().split()
    first_num = ord(first)-97
    end_num = ord(end)-97
    graph[first_num] += [end_num]
m = int(input())
for _ in range(m):
    first, arrow, end = input().split()
    visited = {i:False for i in range(26)}
    first_num = ord(first)-97
    end_num = ord(end)-97
    visited[first_num] = True
    print('T' if DFS(first_num,end_num) else 'F')

