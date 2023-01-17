import sys;sys.setrecursionlimit(100000000)
m=1000000
def z(n,k):
    if k==0:
        if n==0:return 1
        else:return 0
    r=d[n][k]
    if r!=-1:return r
    d[n][k]=(z(n,k-1)+z(n-1,n-k))%m
    return d[n][k]
d=[[-1]*101 for _ in range(101)]
d[0][0]=1
n=int(input())
print(1 if n==1 else 2*z(n,n)%m)