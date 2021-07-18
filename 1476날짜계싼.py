import sys
input = sys.stdin.readline


# E 1~15, S 1~28, M 1~19
E,S,M = map(int,input().split())
cnt=0
while 1:
    if E==S and S==M:
        print(cnt + E)
        break
    E -= 1
    S -= 1
    M -= 1
    if E==0:
        E=15
    if S==0:
        S=28
    if M==0:
        M=19
    cnt+=1