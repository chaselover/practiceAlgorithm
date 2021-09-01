import sys
input = sys.stdin.readline
from collections import deque,defaultdict


# 왜? BFS로 안풀림?
def BFS(start):
    q = deque()
    q.append([start,0])
    vi[start] = True
    a = 0
    while q:
        c_n,d = q.popleft()
        for n_n in g[c_n]:
            if not vi[n_n]:
                vi[n_n]=True
                q.append([n_n,d+1])
                if len(g[n_n])==1:
                    a += d+1
    return a

N = int(input())
g = defaultdict(list)
vi = {i: False for i in range(1,N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a] += [b]
    g[b] += [a]

print("Yes" if BFS(1)&1 else "No")



# '''
# [리프노드-루트노드까지의 거리]의 총 합이 홀수냐 짝수냐를 묻는 문제...인가?
# '''
# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input())
# graphs = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     a, b = map(int, input().split())
#     graphs[a].append(b)
#     graphs[b].append(a)

# q = deque()
# # 노드번호, 거리
# q.append([1,0])
# vi = [0] * (N+1)
# vi[1] = 1

# a = 0
# while q:
#     cur, d = q.popleft()
#     # 리프 여부 체크
#     flag = True
#     for next in graphs[cur]:
#         if not vi[next]:
#             q.append([next, d+1])
#             vi[next] = 1
#             flag = False
#     if flag:
#         a += d

# if a%2:
#     print('Yes')
# else:
#     print('No')