import sys
input = sys.stdin.readline
 
 
seg = [0 for _ in range(2020202)]
 
def init(n,s,e):
    if s==e:
        seg[n] = a[s-1]
        return seg[n]
    mid = (s+e)//2
    seg[n] = init(n*2, s, mid) + init(n*2 + 1, mid + 1, e)
    return seg[n]
 
def update(n,s,e,idx,dif):
    if idx < s or e < idx: return
 
    seg[n] += dif
    if s == e: return
 
    mid = (s+e)//2
    update(n*2,s,mid,idx,dif)
    update(n*2 + 1, mid + 1, e, idx, dif)
 
def getSum(n,l,r,s,e):
    if l <= s and e <= r: return seg[n]
    if e < l or r < s: return 0
    
    mid = (s+e)//2
    return getSum(n*2,l,r,s,mid)+getSum(n*2+1,l,r,mid+1,e)
 
def bs(lo,hi,x):
    lo = 1
    hi = n
    while lo < hi:
        mi = (lo+hi)//2
        if getSum(1,1,mi,1,n) < at[1]:
            lo = mi+1
        else:
            hi = mi
    return hi
 
n = int(input())
a = list(map(int, input().split()))
init(1,1,n)
q = int(input())
for i in range(q):
    at = list(map(int, input().split()))
    if at[0]&1:
        update(1,1,n,at[1],at[2])
        continue
    else:
        print(bs(1,n,at[1]))