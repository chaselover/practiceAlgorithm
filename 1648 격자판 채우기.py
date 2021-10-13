# 비트마스킹 DP
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
DP = [[0] * (1 << M) for num in range(N * M + 1)]
DP[N * M][0] = 1
for num in reversed(range(N * M)):
    for state in range(1 << M):
        if state & 1:
            DP[num][state] = DP[num + 1][state >> 1] % 9901
        else:
            if num < (N-1) * M:
                DP[num][state] += DP[num + 1][(1 << (M - 1)) | (state >> 1)] % 9901
            if num % M < M-1 and not state % 4:
                DP[num][state] += DP[num + 2][state >> 2] % 9901
print(DP[0][0] % 9901)


# 2
n,m=map(int,input().split())
d=[[0]*(1<<m) for i in range(n*m+1)]
d[n*m][0]=1
for i in range(n*m-1,-1,-1):
  for j in range(1<<m):
    if j&1:
      d[i][j]=d[i+1][j>>1]
      continue
    if i<(n-1)*m:
      d[i][j]+=d[i+1][(1<<(m-1))|(j>>1)]
    if i%m<m-1 and not j%4:
      d[i][j]+=d[i+2][j>>2]
print(d[0][0]%9901)

# https://www.acmicpc.net/problem/1648
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
dp = [[-1 for _ in range(1 << m)] for _ in range(n * m)]


def getAnswer(idx, state):
    if idx == n * m:
        return 0 if state else 1

    if dp[idx][state] != -1:
        return dp[idx][state]

    ret = 0
    if state & 1:
        ret += getAnswer(idx + 1, state >> 1)
    else:
        if idx % m < (m - 1) and not (state & 2):
            ret += getAnswer(idx + 2, state >> 2)
        ret += getAnswer(idx + 1, state >> 1 | (1 << (m - 1)))
    ret %= 9901
    dp[idx][state] = ret
    return ret


print(getAnswer(0, 0))

# 4
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def getBit(first, flag,cur):        
    if cur >= n:
        result[first] += [flag]
        return
        
    getBit(first,flag,cur+1)
    if (3<<cur & flag) == 0 and cur+1 < n:
        getBit(first, flag | (3<<cur), cur+2)

def solve(i,flag):
    if i == m:        
        return 1 if flag == setBit else 0

    if dp[i][flag] != -1:
        return dp[i][flag]

    dp[i][flag] = 0
    n_flag = setBit ^ flag

    if not result[n_flag]:
        getBit(n_flag, n_flag, 0)
    
    for j in result[n_flag]:
        dp[i][flag] += solve(i+1, j)
    dp[i][flag] %= 9901
    return dp[i][flag]

n,m = map(int, input().split())
setBit = (1<<n)-1
dp = [[-1]*(1<<n) for i in range(m)]
result = [[] for i in range(1<<n)]

print(solve(0,setBit) % 9901)


# 4
N,M=map(int,input().split())
DP=[[-1]*(1<<M)for i in range(N*M)]
def go(i,n):
    if i==N*M:
        if n:
            return 0
        else:
            return 1
    if DP[i][n]>=0:
        return DP[i][n]
    r=0
    if n&1==1:
        r+=go(i+1,n>>1)
    else:
        r+=go(i+1,(n>>1)+(1<<(M-1)))
        if n&2!=2 and i%M!=M-1:
            r+=go(i+2,n>>2)
    DP[i][n]=r
    return DP[i][n]
print(go(0,0)%9901)