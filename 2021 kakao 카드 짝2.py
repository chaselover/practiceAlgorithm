from collections import deque


def move(board, x, y, dx, dy):
    nx, ny = x + dx, y + dy
    if 0 <= nx < 4 and 0 <= ny < 4:
        if board[nx * 4 + ny] == "0":
            return move(board, nx, ny, dx, dy)
        else:
            return (nx, ny)
    else:
        return (x, y)


def solution(b, r, c):
    answer = 0
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    board = ""
    for row in b:
        board += ''.join(list(map(str, row)))
    q = deque([])
    enter = -1
    q.append((r, c, board, 0, enter))
    state = set()

    while q:
        x, y, board, cnt, e = q.popleft()
        if (x, y, board, cnt, e) in state:
            continue
        state.add((x, y, board, cnt, e))

        cur_position = 4 * x + y
        if board.count('0') == 16:
            return cnt
 
        # 4 방향 이동
        for dx, dy in delta:
            ny, nx = y + dy, x + dx
            if 0 <= nx < 4 and 0 <= ny < 4:
                q.append((nx, ny, board, cnt + 1, e))

        # Ctrl + 4 방향 이동
        for dx, dy in delta:
            nx, ny = move(board, x, y, dx, dy)
            if ny == y and nx == x:
                continue
            q.append((nx, ny, board, cnt + 1, e))

        # enter를 하는 경우
        if board[cur_position] != 0:
            if e == -1:
                n_e = cur_position
                q.append((x, y, board, cnt + 1, n_e))
            else:
                if e != cur_position and board[e] == board[cur_position]:
                    n_b = board.replace(board[e], '0')
                    q.append((x, y, n_b, cnt + 1, -1))

    return answer