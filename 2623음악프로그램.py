import sys
from collections import defaultdict,deque
input = sys.stdin.readline

def topological_sorting():
    queue = deque()
    for i in range(1, N+1):
        if level[i] == 0: 
            queue.append(i)
    while queue:
        cur_order = queue.popleft()
        final_order.append(cur_order)
        for post_order in post_order_table[cur_order]:
            level[post_order] -= 1
            if level[post_order] == 0:
                queue.append(post_order)

N, M = map(int, input().split())
level = [0 for _ in range(N+1)]
post_order_table = defaultdict(list)
final_order = []

for _ in range(M):
    order = list(map(int, input().split()))
    for i in range(1,len(order) - 1): 
        post_order_table[order[i]] += [order[i+1]]
        level[order[i+1]] += 1

topological_sorting()

if len(final_order) != N:
    print(0)
    exit()

for singer in final_order:
    print(singer)

