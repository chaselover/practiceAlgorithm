import sys
input = sys.stdin.readline

N,M = map(int,input().split())
S = {}
for _ in range(N):
    S[input().rstrip()] = 1
cnt=0
for _ in range(M):
    a = input().rstrip()
    try:
        if S[a] ==1:
            cnt+=1
    except:
        continue

print(cnt)