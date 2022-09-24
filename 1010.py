
T = int(input())

for test in range(T):
    N,M = map(int,input().split())
    a,b = 1,1
    for i in range(N):
        a = a*(M-i)
    for i in range(1,N+1):
        b = b*i
    
    ans = int(a/b)

    print(ans)