import sys
input = sys.stdin.readline

def stick_paper(n):
    length = n//10
    dp = [0] * (length+1)
    dp[0],dp[1] = 1,1
    for i in range(2,length+1):
        dp[i] = dp[i-2]*2 + dp[i-1]
    return dp[length]


for test in range(1,int(input())+1):
    print(f'#{test} {stick_paper(int(input()))}')
