import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dnas = [input().rstrip() for _ in range(n)]
nut = ['A','C','G','T']
dp_sum = [[0 for _ in range(4)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        for k in range(4):
            if dnas[i][j] == nut[k]:
                dp_sum[j][k] += 1
                break
result = ''
cnt = 0
for i in range(m):
    tmp = max(dp_sum[i])
    result += nut[dp_sum[i].index(tmp)]
    cnt += n - tmp
print(result)
print(cnt)