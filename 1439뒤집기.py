import sys
input = sys.stdin.readline

s = input().rstrip()
N = len(s)
cnt=0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt+=1
if cnt%2:
    print(cnt//2+1)
else:
    print(cnt//2)