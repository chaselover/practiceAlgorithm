import sys

def fibonacii(n):
    global cnt_0,cnt_1
    if n==0:
        cnt_0 += 1
        return 0
    elif n==1:
        cnt_1 += 1
        return 1
    else:
        return fibonacii(n-1) + fibonacii(n-2)


T = int(sys.stdin.readline())

for test in range(1,T+1):
    n = int(sys.stdin.readline())
    cnt_0 = 0
    cnt_1 = 0
    fibonacii(n)
    print(f'{cnt_0} {cnt_1}')