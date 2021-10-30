def solution(n, jump):
    board = [[0] * n for _ in range(n)]
    size = (n ** 2)
    delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
    arr = [0] * size
    arr[0] = 1
    num = 1
    cnt = 0
    while num < size:
        for i in range(size):
            if not arr[i]:
                cnt += 1
            if cnt == jump:
                num += 1
                arr[i] = num
                cnt = 0
    target_cnt = arr.index(size)
    q = []
    q.append((0, 0, 0, 0))
    while q:
        x, y, d, cnt = q.pop()
        board[x][y] = arr[cnt]
        if cnt == target_cnt:
            answer = [x + 1, y + 1]
            break
        for i in range(d, d + 4):
            i %= 4
            nx, ny = x + delta[i][0], y + delta[i][1]
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                q.append((nx, ny, i, cnt + 1))
                break
    return answer

print(solution(5, 3))