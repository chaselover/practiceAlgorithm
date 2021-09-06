import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
while n > 1:
    if not n%5:
        cnt += n//5
        n = 0
    else:
        n -= 2
        cnt += 1
print(-1 if n else cnt)