from math import ceil,log2
import sys
input = sys.stdin.readline

def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = ( start + end ) // 2
    l = query(node*2, start, mid, left, right)
    r = query(node*2+1, mid+1, end, left, right)
    return l+r 

def update(node, start, end, idx):
    if idx < start or end < idx:
        return 0
    
    if start == end:
        tree[node] = 1
        return tree[node]
    
    mid = (start + end)//2
    update(node*2, start, mid, idx)
    update(node*2+1,mid+1,end, idx)
    tree[node] = tree[node*2] + tree[node*2+1]
    return tree[node]

n = int(input())
arr = input().split()

idx = 0
dic = {}
for num in input().split():
    dic[num] = idx
    idx += 1

h = int(ceil(log2(n))) + 1
t_size = 1 << h

tree = [0] * t_size

answer = 0
for num in arr:
    s_idx = dic[num]
    answer += query(1, 0, n-1, s_idx, n-1)

    update(1, 0, n-1, s_idx)

print(answer)



#######################
import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = [i + 1 for i in range(N)]
B = []
maps = {}
for i in range(N):
    maps[a[i]] = i + 1
for j in b:
    B.append(maps[j])
tree = [0] * (N + 1)
def sum(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)
    return res
def update(i, x):
    while i < len(tree):
        tree[i] += x
        i += (i & -i)
result = 0
for b in B:
    update(b, 1)
    result += sum(N) - sum(b)
print(result)



###########################
import sys

def sum(idx):
    ans = 0
    while idx > 0:
        ans += tree[idx]
        idx -= (idx & -idx)
    return ans

def update(idx, val):
    while idx < len(a):
        tree[idx] += val
        idx += (idx & -idx)

N = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
b = [0] + list(map(int, sys.stdin.readline().split()))
tree = [0] * (N+1)
rev_a = [-1] * (1000001)
for i in range(1, len(a)):
    rev_a[a[i]] = i

ans = 0
for i in range(1, len(b)):
    idx = rev_a[b[i]]
    ans += sum(N) - sum(idx)
    update(idx, 1)

print(ans)



###############################
import sys
input = sys.stdin.readline
mis = lambda: map(int, input().split())

def update(idx, val):
    idx = idx + L - 1
    seg[idx] = val
    idx //= 2
    while idx:
        seg[idx] = seg[idx*2] + seg[idx*2+1]
        idx //= 2

def query(l, r):
    l, r = l + L - 1, r + L - 1
    ret = 0
    while l <= r:
        if l%2 == 1:
           ret += seg[l]
           l += 1
        if r%2 == 0:
            ret += seg[r]
            r -= 1
        l//=2; r//=2
    return ret

N = int(input())
L = 2 ** N.bit_length()
seg = [0] * (2*L)
d = [-1] * 1000001
org = list(mis())
for i in range(N):
    d[org[i]] = i
ans = 0
nxt = list(mis())
for i in range(N):
    ans += query(d[nxt[i]], N-1)
    update(d[nxt[i]], 1)
print(ans)


