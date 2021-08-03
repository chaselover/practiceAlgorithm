import sys
input = sys.stdin.readline
from math import ceil,log2

def init(node,start,end):
    if start==end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start+end)//2
    tree[node] = min(init(node*2,start,mid),init(node*2+1,mid+1,end))
    return tree[node]

def query(node,start,end,left,right):
    if start > right or end < left:
        return float('inf')
    if left <=start and end <= right:
        return tree[node]
    
    mid = (start+end)//2
    return min(query(node*2,start,mid,left,right),query(node*2+1,mid+1,end,left,right))

N,M = map(int,input().split())
h = int(ceil(log2(N)))
t_size = 1<<(h+1)
arr = []
tree = [0] * t_size

for _ in range(N):
    arr.append(int(input()))

init(1,0,N-1)

for _ in range(M):
    a,b = map(int,input().split())
    print(query(1,0,N-1,a-1,b-1))