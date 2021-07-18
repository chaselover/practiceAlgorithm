import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]	# 상하좌우
dy = [0, 0, -1, 1]

def DFS(x, y):
    global answer
    visited[x][y] = 1	# 방문 체크
    for d in range(4):
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= X < N and 0 <= Y < M:	# 다음 타겟이 matrix 안에 있으면
            if matrix[X][Y] == matrix[x][y]:		# 값(색깔)이 같으면
                if visited[X][Y] == 0:	# 아직 방문한 적이 없다면
                    my_snake.append([X, Y])		#방문 순서에 기록한다
                    DFS(X, Y)	# 방문하러 가기 (재귀)
                    my_snake.pop()	# 방문 순서에서 제외한다
                else:		# 방문한 적이 있다면
                    if X == my_snake[-2][0] and Y == my_snake[-2][1]:	# 바로 전에 방문한 곳이면
                        pass
                    else:	# 바로 전은 아닌데 언젠가 방문한 적이 있음 (사이클 형성)
                        answer = 'Yes'	# 답을 바꾸고 바로 빠져나간다
                        return
        if answer == 'Yes':
            return

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]	# 방문 체크용
answer = 'No'	# 기본값은 No

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:	# 해당 구역을 방문한 적이 없다면
            my_snake = [[i, j]]	# 방문 순서 기록용
            DFS(i, j)
        if answer == 'Yes':	# 답이 바뀌면 바로 빠져나온다.
            break
    if answer == 'Yes':
        break

print(answer)