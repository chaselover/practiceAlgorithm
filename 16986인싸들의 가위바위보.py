import sys
from itertools import permutations

# 다음엔 꼭 구현하는걸로.

def DFS(pi1,pi2,index,win,player):
    global result
    # 지우 승
    if win[0] == K:
        result = 1
        return
    # 경희 민호 승
    if win[1] == K or win[2] == K:
        return
    if index[0] == N:
        return
    #다음 차례 상대방을 구할 경우, 지우, 경희, 민호를 각각 0,1,2라고 했을 때 
    #총 합(3)에서 출전 했던 선수의 합을 빼면 다음 차례에 나올 선수의 번호가 나옴
    pi3 = 3 - (pi1+pi2) 
    # 각 플레이어가 이번에 낼 손동작
    pv1 = player[pi1][index[pi1]] - 1
    pv2 = player[pi2][index[pi2]] - 1
    # 다음번 낼 손동작 idx 하나 늘려줌.(다음 턴)
    index[pi1] += 1
    index[pi2] += 1
    if game_rule[pv1][pv2] == 2 or (game_rule[pv1][pv2] == 1 and pi1 > pi2) : #pi1이 이겼을 경우
        win[pi1] += 1
        DFS(pi1, pi3, index, win,player)
    elif (game_rule[pv1][pv2] == 1 and pi1 < pi2) or game_rule[pv1][pv2] == 0: #pi2가 이겼을 경우
        win[pi2] += 1
        DFS(pi2, pi3, index, win,player)

N,K = map(int,sys.stdin.readline().split())
game_rule = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
gyung_hee = list(map(int,sys.stdin.readline().split()))#경희
min_ho = list(map(int,sys.stdin.readline().split()))#민호
target = [i+1 for i in range(N)] # 지우가 낼 경우의 수.

for jiwoo in permutations(target,N):#지우가 N개를 뽑는 순열(내는 순서가 바뀌는 모든 경우의 수.)
    player = [jiwoo,gyung_hee,min_ho] # 각자 3명이 1회부터 N회까지 내는 가위바위보의 패턴.
    index = [0,0,0] #지우, 경희, 민호가 다음 번에 낼 손동작 index
    win = [0,0,0] #지우, 경희, 민호 이긴 횟수
    result = 0
    DFS(0,1,index,win,player)
    if result == 1:
        print(1)
        break
else:
    print(0)