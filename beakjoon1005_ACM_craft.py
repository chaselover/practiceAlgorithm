import collections as col


T = int(input())

for test in range(T):
    N,K= map(int,input().split())
    D = [0] + list(map(int,input().split()))
    order = col.defaultdict(list)
    dp = [0]*(N+1)

    for _ in range(K):
        X,Y = map(int,input().split())
        order[Y].append(X)

    finish = int(input())
    for i in range(1,N+1):      
        if i not in order:
            dp[i] = D[i]
    for key in order:
        s = []
        if order[key]:
            for adj in order[key]:
                s.append(dp[adj])
            dp[key] = max(s) +D[key]
    
    print(dp)