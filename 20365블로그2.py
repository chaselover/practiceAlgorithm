import sys
input = sys.stdin.readline

N = int(input())
s = input().rstrip()
cnt = {'B': 0,'R': 0}
cnt[s[0]] += 1
for i in range(1,N):
    if s[i] != s[i-1]:
        cnt[s[i]] += 1
print(min(cnt['B'],cnt['R'])+1)