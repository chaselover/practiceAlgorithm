import sys
input = sys.stdin.readline

A, B = map(int, input().split())

cnt = 1
while A != B:
    if A > B or (B % 10 != 1 and B % 2 != 0):
        cnt = -1
        break
    if B & 1:
        B //= 10
        cnt += 1
    else:
        B //= 2
        cnt += 1
    
print(cnt)