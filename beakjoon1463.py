import sys

N=int(sys.stdin.readline())
cnt=0
bag=[3,5]

while N != 0:
    if N%3==0:
        cnt += N//3
        N=0
    elif N%2==0:
        cnt += N//2
        N=0
    elif N < 0:
        print(-1)
        break
    else:
        N = N-1
        cnt += 1

if N==0:   
    print(cnt)