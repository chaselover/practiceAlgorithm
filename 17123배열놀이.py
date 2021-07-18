import sys
input = sys.stdin.readline

T = int(input())

for test in range(T):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]


    for _ in range(M):
        r1,c1,r2,c2,v = map(int,input().split())
        for i in range(r1-1,r2):
            for j in range(c1-1,c2):
                matrix[i][j] +=v


    for i in range(N):
        print(sum(matrix[i]), end=" ")
    print()
    for j in range(N):
        print(sum(matrix[m][j] for m in range(N)), end=" ")
    print()