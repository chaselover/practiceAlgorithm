n, k = map(int, input().split())
dp = [[0] * 201 for i in range(201)]
# 1열은 모두 1. 1행도 마찬가지.
for i in range(201):
    dp[i][1] = 1
#j는 n(행) i는 k(열) 
# n은j, k는i 일때 답은 k-1열일때 n=0~n=j일때까지 모든 dp의 합. 
for i in range(1, 201):
    for j in range(201):
        for l in range(j + 1):
            dp[j][i] += dp[l][i - 1]
print(dp[n][k] % 1000000000)


# dp에 표를 그린다. 가로 1열, 세로 1열 (n,k) = (0,1)시작부터 끝까지 쭉 그림.
