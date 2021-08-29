def cal_team(lst):
    sum_team = 0
    for _i in range(len(lst)):
        for _j in range(len(lst)):
            if _i != _j:
                i, j = lst[_i], lst[_j]
                sum_team += board[i][j]
    return sum_team

def comb(s, cnt, n):
    global min_ans, visited
    if cnt == n:
        team1, team2 = [], []
        for i in range(N):
            if visited[i]:
                team1.append(i)
            else:
                team2.append(i)
        if len(team1) * len(team2) == 0:
            return
        sum_team1 = cal_team(team1)
        sum_team2 = cal_team(team2)
        min_ans = min(min_ans, abs(sum_team1 - sum_team2))
        return
    for i in range(s, N):
        visited[i] = True
        comb(i+1, cnt+1, n)
        visited[i] = False

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
min_ans = 1e9
team1, team2 = [], []

visited = [False] * N
for i in range(1, N//2+1):
    comb(0, 0, i)
print(min_ans)