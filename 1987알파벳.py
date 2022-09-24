import sys
input = sys.stdin.readline


def bfs(x, y):
    q = set([(x, y, board[x][y])])
    check[x][y] = board[x][y]
    answer = 1
    while q:
        x, y, string = q.pop()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in string:
                new_string = string + board[nx][ny]
                if check[nx][ny] != new_string:
                    check[nx][ny] = new_string
                    q.add((nx, ny, new_string))
                    answer = max(answer, len(string) + 1)
                    if answer == 26:
                        return 26
    return answer

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
check = [[''] * C for _ in range(R)]
print(bfs(0, 0))