T = int(input())


def coloringGraph():
    N,E,M = map(int,input().split())

    G =[[0 for _ in range(N)]for _ in range(N)]

    for _ in range(E):
        x,y = map(int,input().split())
        G[x-1][y-1] = 1
        G[y-1][x-1] = 1

    for i in range(N):
        if sum(G[i]) > M:
            return 0

    return 1


for testcase in range(T):
    print("#{} {}".format(testcase+1, coloringGraph()))