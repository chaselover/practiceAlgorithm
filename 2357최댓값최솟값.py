import sys
input = sys.stdin.readline
from math import ceil,log2

def init_min_tree(node,start,end):
    if start==end:
        min_tree[node] = a[start]
        return min_tree[node]
    mid= (start+end)//2
    min_tree[node] = min(init_min_tree(node*2,start,mid),init_min_tree(node*2+1,mid+1,end))
    return min_tree[node]

def init_max_tree(node,start,end):
    if start==end:
        max_tree[node] = a[start]
        return max_tree[node]
    mid= (start+end)//2
    max_tree[node] = max(init_max_tree(node*2,start,mid),init_max_tree(node*2+1,mid+1,end))
    return max_tree[node]

def query_min(node,start,end,left,right):
    if start > right or end < left:
        return float('inf')
    if left <= start and end <= right:
        return min_tree[node]
    mid= (start+end)//2
    return min(query_min(node*2,start,mid,left,right),query_min(node*2+1,mid+1,end,left,right))

def query_max(node,start,end,left,right):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return max_tree[node]
    mid= (start+end)//2
    return max(query_max(node*2,start,mid,left,right),query_max(node*2+1,mid+1,end,left,right))


N,M = map(int,input().split())
a = []
h = int(ceil(log2(N)))
min_tree = [0]*(1<<h+1)
max_tree = [0]*(1<<h+1)
for _ in range(N):
    a.append(int(input()))

init_min_tree(1,0,N-1)
init_max_tree(1,0,N-1)

for _ in range(M):
    left,right = map(int,input().split())
    print(query_min(1,0,N-1,left-1,right-1),end=" ")
    print(query_max(1,0,N-1,left-1,right-1))
