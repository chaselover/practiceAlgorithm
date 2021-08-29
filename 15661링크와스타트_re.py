
import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    global ans
    # 반 나눠지면 start, link팀 합 구해서 차이 절댓값의 최솟값 전역변수 ans에 최신화 시켜줌.
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n-1):
            for j in range(i+1,n):
                if check[i] and check[j]:
                    start += a[i][j] + a[j][i]
                elif not check[i] and not check[j]:
                    link += a[i][j] + a[j][i]
        ans = min(ans, abs(start - link))
# 그냥 check 가 1인거 반 0인거 반 나누기만함.
    for i in range(idx, n):
        if check[i]:
            continue
        check[i] = 1
        dfs(i + 1, cnt + 1)
        check[i] = 0


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

check = [0 for _ in range(n)]
ans = sys.maxsize
dfs(0, 0)
print(ans)