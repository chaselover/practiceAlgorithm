import sys
input = sys.stdin.readline

N = int(input())
if N==1:
    print(4)
    print(1,1,0,1)
    exit()
max_len = 0
for i in range(1,N):
    dp = [N,i]
    for j in range(2,N):
        tmp = dp[j-2] - dp[j-1]
        if tmp < 0:
            if len(dp) > max_len:
                max_len = len(dp)
                max_arr = dp
            break
        dp.append(tmp)
print(max_len)
print(*max_arr)