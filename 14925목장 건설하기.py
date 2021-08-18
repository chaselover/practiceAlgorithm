import sys
input = sys.stdin.readline

# 가장 큰 정사각형 문제와 같은 문제. 위 좌, 대각 안쪽 중 가장 변의 길이가 짧은 변에 하나를 추가시켜주는 방식이며
# 장애물을 만나면 다시 0부터 시작한다.
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
dp_length = [[0 for _ in range(N+1)] for _ in range(M+1)]
max_length = 0
for i in range(1,M+1):
    for j in range(1,N+1):
        if not matrix[i-1][j-1]:
            dp_length[i][j] = min(dp_length[i-1][j],dp_length[i][j-1],dp_length[i-1][j-1]) + 1
            max_length = max(dp_length[i][j], max_length)
print(max_length)