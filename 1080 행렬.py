import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, list(input().rstrip()))) for _ in range(N)]
B = [list(map(int, list(input().rstrip()))) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if i < N - 2 and j < M - 2:
            if A[i][j] != B[i][j]:
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        A[x][y] ^= 1
                cnt += 1
        else:
            if A[i][j] != B[i][j]:
                print(-1)
                exit()
print(cnt)