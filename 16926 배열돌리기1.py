import sys
input = sys.stdin.readline

def rotate(start):

    #init_tmp
    top = matrix[start][start]
    left = matrix[N-start-1][start]
    bottom = matrix[N-start-1][M-start-1]
    right = matrix[start][M-start-1]

    # top
    for i in range(start+1,M-start):
        matrix[start][i-1] = matrix[start][i]
    # left
    for i in range(N-start-1,start,-1):
        matrix[i][start] = matrix[i-1][start]
    # bottom
    for i in range(M-start-1,start+1,-1):
        matrix[N-start-1][i] = matrix[N-start-1][i-1]
    # right
    for i in range(start+1,N-start):
        matrix[i-1][M-start-1] = matrix[i][M-start-1]
    # finish
    matrix[start+1][start] = top
    matrix[N-start-1][start+1] = left
    matrix[N-start-2][M-start-1] = bottom
    matrix[start][M-start-2] = right

N, M, R = map(int,input().split())
size = 2 * N + 2 * M - 4
matrix = [list(map(int, input().split())) for _ in range(N)]
short = N if N <= M else M

for n_th in range(short//2):
    for _ in range(R%(size-8*n_th)):
        rotate(n_th)

for row in matrix:
    print(*row)