
# # 위상정렬 싸이클 있으면 안돌아감. -> 틀린풀이.
# import sys
# from collections import deque
# input = sys.stdin.readline

# N, M = map(int, input().split())
# parents = {i: [] for i in range(1,N+1)}
# childs = {i: 1 for i in range(1,N+1)}
# level = {i: 0 for i in range(1,N+1)}
# for _ in range(M):
#     a, b = map(int, input().split())
#     parents[a] += [b]
#     level[b] += 1
# queue = deque()
# for i in range(1,N+1):
#     if not level[i]:
#         queue.append(i)

# while queue:
#     cur_node = queue.popleft()
#     for next_node in parents[cur_node]:
#         level[next_node] -= 1
#         childs[next_node] += childs[cur_node]
#         if not level[next_node]:
#             queue.append(next_node)

# max_num = 0
# ans = []
# for node in childs:
#     if childs[node] > max_num:
#         max_num = childs[node]
#         ans.clear()
#         ans.append(node)
#     elif childs[node] == max_num:
#         ans.append(node)
# print(*ans)


from collections import deque
import sys
input = sys.stdin.readline
def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for _ in range(n + 1)]
    visit[start] = 1
    cnt = 1
    while q:
        st = q.popleft()
        for i in s[st]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                q.append(i)
    return cnt
n, m = map(int, input().split())
s = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    s[b].append(a)
result = []
max_cnt = 0
for i in range(1, n + 1):
    tmp = bfs(i)
    if max_cnt == tmp:
        result.append(i)
    if max_cnt < tmp:
        max_cnt = tmp
        result = []
        result.append(i)
print(*result)