j=int
def g(x,y,c):
    return x+y if c=='+'else x-y if c=='-'else x*y
def f(i,c):
    return c if i>=n else max(f(i+2,g(c,j(s[i]),s[i-1])),f(i+4,g(c,g(j(s[i]),j(s[i+2]),s[i+1]),s[i-1]))if i<n-2 else -99)
n,s=j(input()),input()
print(f(2,j(s[0])))


# 다른코드 DP
# N = int(input())
# ev = input()
# dp = [int(ev[0])] + [-10**9] * (N // 2)
# dp2 = [int(ev[0])] + [10**9] * (N // 2)
# for i in range(1, N//2 + 1):
#     for j in range(max(0, i - 2),i):
#         op = ev[j*2 + 1]
#         R = eval(ev[j * 2 + 2: i * 2 + 1])
#         dp[i] = max(dp[i], eval(str(dp[j]) + op + str(R)))
#         dp[i] = max(dp[i], eval(str(dp2[j]) + op + str(R)))
#         dp2[i] = min(dp2[i], eval(str(dp[j]) + op + str(R)))
#         dp2[i] = min(dp2[i], eval(str(dp2[j]) + op + str(R)))
# print(dp[-1])

