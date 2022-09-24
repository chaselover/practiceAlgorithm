import sys
input = sys.stdin.readline

N, K = map(int,input().split())
X_list = list(map(int,input().split()))


# X_list 숫자 갯수 저장.
x_sum = [0]*N
for jump in X_list:
    x_sum[jump] += 1


# 각 위치에서 가지는 숫자값.즉 배열 a완성.
x_dp = [x_sum[1]]*N
for i in range(2,N):
    for j in range(0,N,i):
        x_dp[j] += x_sum[i]


# 누적합
dp = [0] * N
dp[0] = K
for i in range(1,N):
    dp[i] = dp[i-1] + x_dp[i]


# 출력은 Q줄.
# L,R이 주어졌을 때 a[L] + a[L+1] + ... + a[R] 출력
for _ in range(int(input())):
    L,R = map(int,input().split())
    print(dp[R]-dp[L-1] if L else dp[R])

    


