

def solution(board):
    global answer
    n = len(board)
    delta = ((1, 0), (0, 1))
    answer = 0
    
    def dfs(x, y, cnt):
        global answer
        if (x, y) == (n-1, n-1):
            answer = max(answer, cnt)
            return
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny]:
                    dfs(nx, ny, cnt + board[nx][ny])
                else:
                    dfs(nx, ny, cnt)
                    dfs(nx, ny, -cnt)
                    
    dfs(0, 0, board[0][0])     
    return answer