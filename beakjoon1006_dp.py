import sys, collections
T = int(sys.stdin.readline())

for test in range(T):

    N,M,K= map(int,sys.stdin.readline().split())

    air = collections.defaultdict(list)
    c = [0]*N
    t = [0]*N

    for _ in range(K):
        u,v,c,d = map(int,sys.stdin.readline().split())
        air[u].append(v)

    print(air[1])