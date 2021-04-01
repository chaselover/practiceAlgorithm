import collections
 
 
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
 
    list_high = []
    height_max = 0
 
    for i in range(N):
        for j in range(N):
            if board[i][j] > height_max:
                list_high = [(i, j)]
                height_max = board[i][j]
            elif board[i][j] == height_max:
                list_high.append((i, j))
 
    adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
 
    visit_1 = [False] * (N**2)
    queue = collections.deque([])
    for i, j in list_high:
        visit_2 = visit_1[:]
        visit_2[N*i+j] = True
        queue.append((i, j, height_max, visit_2, False))
 
    answer = 0
    while queue:
        answer += 1
 
        for _ in range(len(queue)):
            idx1, idx2, height, visit_3, changed = queue.popleft()
 
            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < N and visit_3[N*nxt1+nxt2] is False:
                    if board[nxt1][nxt2] < height:
                        visit_4 = visit_3[:]
                        visit_4[N*nxt1+nxt2] = True
                        queue.append((nxt1, nxt2, board[nxt1][nxt2], visit_4, changed))
                    elif not changed and board[nxt1][nxt2] - K < height:
                        visit_4 = visit_3[:]
                        visit_4[N*nxt1+nxt2] = True
                        queue.append((nxt1, nxt2, height-1, visit_4, True))
 
    print('#{} {}'.format(t, answer))