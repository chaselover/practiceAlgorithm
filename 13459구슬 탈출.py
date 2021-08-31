from collections import deque


# 벽이나 구멍이 나올때까지 굴린다.
# 굴린 거리만큼 c에 저장.
def move(i, j, dx, dy):
    c = 0
    while s[i + dx][j + dy] != "#" and s[i][j] != "O":
        i += dx
        j += dy
        c += 1
    return i, j, c


def bfs():

    while q:
        ri, rj, bi, bj, d = q.popleft()
        # 10번 넘게 돌리면 종료.
        if d > 10:
            break
        # 구슬 두개를 같이 돌린다. 매 분기마다 4방향을 모두 검사한다.
        for i in range(4):
            nri, nrj, rc = move(ri, rj, dx[i], dy[i])
            nbi, nbj, bc = move(bi, bj, dx[i], dy[i])
            # 파란구슬이 O가 아니면서 빨간구슬이 O면 종료. 
            if s[nbi][nbj] != "O":
                if s[nri][nrj] == "O":
                    print(1)
                    return
                # 아니면서 두 구슬의 위치가 겹칠때 이동한 거리가 긴놈을 -1칸 뒤로 위치시킴.
                if nri == nbi and nrj == nbj:
                    if rc > bc:
                        nri -= dx[i]
                        nrj -= dy[i]
                    else:
                        nbi -= dx[i]
                        nbj -= dy[i]
                # 똑같은 배치가 한번도 안나왔다면 분기로 진입.
                if not visit[nri][nrj][nbi][nbj]:
                    visit[nri][nrj][nbi][nbj] = True
                    q.append([nri, nrj, nbi, nbj, d + 1])
    print(0)


n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]
s = []
# 구슬 최초위치 저장.
for i in range(n):
    a = list(input())
    s.append(a)
    for j in range(m):
        if a[j] == "R":
            ri, rj = i, j
        if a[j] == "B":
            bi, bj = i, j
q = deque()
# 탐색.
q.append([ri, rj, bi, bj, 1])
visit[ri][rj][bi][bj] = True
bfs()