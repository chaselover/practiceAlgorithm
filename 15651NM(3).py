
n,m = list(map(int,input().split()))
s = []

def dfs(depth):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(1,n+1):
            s.append(i)
            dfs(depth+1)
            s.pop()
dfs(0)