import sys; INP = sys.stdin.readline
import heapq
import bisect
import math

# segment
def init(l, r, node):
    if l == r:
        tree[node].append(nums[l][1])
        return
    mid = (l+r)//2
    init(l, mid, node*2)
    init(mid+1, r, node*2+1)
    tree[node] = list(heapq.merge(tree[node*2], tree[node*2+1]))

def query(ql, qr, k, node, nl, nr):
    if nl==nr:
        return tree[node][0]
    mid = (nl+nr)//2
    cnt = bisect.bisect_right(tree[node*2], qr) - bisect.bisect_left(tree[node*2], ql)

    if cnt >= k:
        return query(ql, qr, k, node*2, nl, mid)
    else:
        return query(ql, qr, k-cnt, node*2+1, mid+1, nr)


N, M = map(int, INP().split())
a = list(map(int, INP().split()))
nums = []
for i in range(N):
    nums.append((a[i], i))
nums.sort()
h = int(math.ceil(math.log2(N)))
tree = [[] for _ in range(1 << (h+1))]
init(0, N-1, 1)

for i in range(M):
    s, e, k = map(int, INP().split())
    print(a[query(s-1,e-1,k,1,0,N-1)])