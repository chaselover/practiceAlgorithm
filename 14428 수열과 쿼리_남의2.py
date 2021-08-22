import sys
pin = sys.stdin.readline
INF = (1000000001,0)

def update(i,x):
    n = i+tsize-1
    tree[n] = (x,i)
    while n>1:
        n //= 2
        tree[n] = min(tree[n*2],tree[n*2+1])

def rmin(L,R):
    L += tsize-1; R += tsize-1
    ans = INF
    while L <= R:
        if L%2==1: ans = min(ans,tree[L]); L += 1
        if R%2==0: ans = min(ans,tree[R]); R -= 1
        L //= 2; R //= 2
    return ans[1]

N = int(pin())
tsize = 1
while tsize < N: tsize *= 2
tree = [INF for _ in range(tsize*2)]
A = [*map(int,pin().split())]
for n in range(N): update(n+1,A[n])
M = int(pin())
for m in range(M):
    Q,a,b = map(int,pin().split())
    if Q==1: update(a,b)
    else: print(rmin(a,b))