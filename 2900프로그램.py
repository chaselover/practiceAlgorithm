import sys
input = sys.stdin.readline

N,K = map(int,input().split())
X_list = list(map(int,input().split()))

# 출력은 Q줄.
# L,R이 주어졌을 때 a[L] + a[L+1] + ... + a[R] 출력
for _ in range(int(input())):
    L,R = map(int,input().split())
    ans = 0
    if L:
        for jump in X_list:                                         # 함수 K번 호출
            ans += R//jump - (L-1)//jump
    else:                                                           # L에서 R사이에 jump의 갯수 +=해주면 됨.
        for jump in X_list:
            ans += R//jump +1

    print(ans)    


