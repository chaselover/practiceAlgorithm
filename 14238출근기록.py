import sys
input = sys.stdin.readline


S = input().strip()
n = len(S)

dp = [[[[[0 for _ in range(3)] for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

ans = [0] * 50
def go(a, b, c, p1, p2):
    if a < 0 or b < 0 or c < 0:
        return False
    if a == 0 and b == 0 and c == 0:
        return True
    if dp[a][b][c][p1][p2]:
        return False
    dp[a][b][c][p1][p2] = True
    ans[n-a-b-c] = 'A'
    if go(a - 1, b, c, 0, p1):
        return True
    if p1 != 1:
        ans[n-a-b-c] = 'B'
        if go(a, b - 1, c, 1, p1):
            return True
    if p1 != 2 and p2 != 2:
        ans[n-a-b-c] = 'C'
        if go(a, b, c - 1, 2, p1):
            return True
    return False



an = 0
bn = 0
cn = 0
for s in S:
    if s == 'A':
        an += 1
    elif s == 'B':
        bn += 1
    elif s == 'C':
        cn += 1
if go(an, bn, cn, 0, 0):
    print(''.join(ans[:n]))
else:
    print(-1)