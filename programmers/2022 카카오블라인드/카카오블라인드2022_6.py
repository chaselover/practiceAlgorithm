
def magic(cnt, s,board):
    tp, x1, y1, x2, y2, depth = s
    flag = 0
    if tp==1:
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if board[i][j] > 0:
                    flag = 1
                board[i][j] -= depth
                if flag and board[i][j] <= 0:
                    cnt += 1
                flag = 0
    else:  
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if board[i][j] <= 0:
                    flag = 1
                board[i][j] += depth
                if flag and board[i][j] > 0:
                    cnt -= 1
                flag = 0
    return cnt, board


def solution(board, skill):
    global cnt
    # N,M크기의 행렬모양 맵.
    cnt = 0
    for change in skill:
        cnt, board = magic(cnt, change, board)
    return len(board) * len(board[0]) - cnt
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))