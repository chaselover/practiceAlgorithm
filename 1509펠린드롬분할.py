import sys
input = sys.stdin.readline

strings = input().rstrip()
n = len(strings)

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
result = [float('inf')] * (n+1)
result[0] = 0

# 일단 자기자신을 분할로 갖는 펠린드롭
for i in range(1, n+1):
    dp[i][i] = 1

# 전놈이랑 나랑 같으면 하나
for i in range(1, n):
    if strings[i-1] == strings[i]:
        dp[i][i+1] = 1

# i는 크기. j는 시작점. j에서 i만큼의 길이를 가진 문자열이 펠린드롬이냐를 확인.
# dp[j+1][i+j-1] 즉 문자열 j-1과 j+i-1이 같고 그 안쪽 dp가 1을 가질때 스트링을 포함한 문자열도 펠린드롭.
for i in range(2, n):
    for j in range(1, n+1-i):
        if strings[j-1] == strings[j+i-1] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

# i를 진행하면서 그 뒤쪽의 result값에 대해 j가 계속 최신화를 시켜주며 최솟값으로 갱신시킴.
for i in range(1, n+1):
    result[i] = min(result[i], result[i-1] + 1)
# result[i-1]+1인 이유는 result[i-1]까지의 팰린드롭에 j부터 i까지의 팰린드롭 한개를 더하는 것이기 때문이다
    for j in range(i+1, n+1):
        if dp[i][j] != 0:
            # 팰린드롭이면
            result[j] = min(result[j], result[i-1] + 1)

print(result[n])