import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
# 1~M-2번 인덱스, 1~N-2번 인덱스의 합이 가장 작은 배열과 가생이에 있는 합이 가장 큰 배열과 교환을 해준다.
# 열검사 -> (1~N-2)*2 + 0 + N-1 의 합을 검사. 가장 작은 열과 가생이에 있는 열 2개의 차이중 큰..
# 행검사
total_sum = (sum(matrix[0])*2 - (matrix[0][0]+matrix[0][M-1])) + (sum(matrix[N-1])*2 - (matrix[N-1][0]+matrix[N-1][M-1]))
max_row = max((sum(matrix[0])*2 - (matrix[0][0]+matrix[0][M-1])),(sum(matrix[N-1])*2 - (matrix[N-1][0]+matrix[N-1][M-1])))
min_row = float('inf')
for i in range(1,N-1):
    sum_row = sum(matrix[i])*2 - matrix[i][0] - matrix[i][M-1]
    total_sum += sum_row*2
    min_row = min(min_row,sum_row)

row_change_value = max_row - min_row
# 열검사
matrix = list(map(list,zip(*matrix)))
N,M = M,N
max_col = max((sum(matrix[0])*2 - (matrix[0][0]+matrix[0][M-1])),(sum(matrix[N-1])*2 - (matrix[N-1][0]+matrix[N-1][M-1])))
min_col = float('inf')
for i in range(1,N-1):
    sum_col = sum(matrix[i])
    min_col = min(min_col,sum_col*2 - matrix[i][0] - matrix[i][M-1])

col_change_value = max_col - min_col

answer = max(total_sum,total_sum+max(row_change_value,col_change_value))
print(answer)