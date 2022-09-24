import sys
input = sys.stdin.readline

N, T = map(int, input().split()) 
score_table = [list(map(int,input().split())) for _ in range(N)] 
dp = [[0]*(T+1) for _ in range(N+1)]


for i in range(1, N+1):                         #N개 과목에 대해 누적값 검사
    for j in range(1, T+1):                     #j시간에 대해 누적값 검사.
        if j >= score_table[i-1][0]:            #i번째 과목을 공부할 수 있는 시간이 되면 공부 시작.
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-score_table[i-1][0]] + score_table[i-1][1]) 
        else: 
            dp[i][j] = dp[i-1][j]

print(dp[N][T])

