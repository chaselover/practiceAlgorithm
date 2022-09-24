

n = int(input())

dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1  #i(n값)+1되면 cnt도 +1

    if i%2 == 0 and dp[i] > dp[i//2] + 1 : #n이 2의 배수이면 그전 2의배수의 cnt+1
        dp[i] = dp[i//2]+1
        
    if i%3 == 0 and dp[i] > dp[i//3] + 1 : #n이 3의 배수이면 그전 3의배수의 cnt+1
        dp[i] = dp[i//3] + 1
        
print(dp[n]) #n까지 반복하고 n의 cnt값 출력