import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
sa = [0]
sb = [0]
e = [True for i in range(2000)]
result = []
def era():
    e[1] = False
    for i in range(2, 50):
        if e[i] == True:
            for j in range(i * 2, 2000, i):
                e[j] = False
era()
def dfs(start):
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in s_[start]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = start
            return 1
    return 0
for i in range(n):
    if s[0] % 2 == s[i] % 2:
        sa.append(s[i])
    else:
        sb.append(s[i])
s_ = [[] for i in range(len(sa))]
for i in range(1, len(sa)):
    for j in range(1, len(sb)):
        if e[sa[i] + sb[j]]:
            s_[i].append(j)
for i in s_[1]:
    d = [0 for _ in range(len(sb))]
    d[i] = 1
    cnt = 1
    for j in range(1, len(sa)):
        visit = [0 for _ in range(len(sa))]
        visit[1] = 1
        cnt += dfs(j)
    if cnt == n // 2:
        result.append(sb[i])
if not result:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i, end=" ")