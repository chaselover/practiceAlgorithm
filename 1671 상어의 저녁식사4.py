def can_eat(i,j):
    if shark[i][0]>=shark[j][0] and shark[i][1]>=shark[j][1] and shark[i][2]>=shark[j][2]: return True
    return False

def dfs(i):
    global visit,shark_eated
    if visit[i]: return 0
    visit[i] = True
    for j in shark_eat[i]:
        if shark_eated[j] == -1 or dfs(shark_eated[j]):
            shark_eated[j]=i
            return 1
    return 0

n = int(input())
shark = [list(map(int,input().split())) for _ in range(n)]
shark_eat = [[] for _ in range(n)]
visit = [False]*n
shark_eated = [-1]*n
count_die = 0

for i in range(n):
    for j in range(n):
        if can_eat(i,j):
            if shark[i] == shark[j] and i <= j: continue
            shark_eat[i].append(j)

for i in range(2):
    for j in range(n):
        visit = [False]*n
        count_die += dfs(j)

print(n-count_die)
