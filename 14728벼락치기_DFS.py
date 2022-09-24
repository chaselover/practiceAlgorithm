import sys
input = sys.stdin.readline


N,T = map(int,input().split())
# 여러 단원을 융합한 문제는 출제하지 않는다.
# 한 단원에 한 문제를 출제한다. 단 그 단원에 모든 내용을 알고 있어야 풀수 있다.

score_table = [list(map(int,input().split())) for _ in range(N)] 
score_table.append([1000000000,0])
check = [False]*101
max_score = 0

def DFS(v,sum_score,sum_time,last_score):
    global max_score
    if sum_time > T:
        max_score = max(max_score,(sum_score-last_score))
        return 
    for i in range(v,N+1):
        if not check[i]:
            check[i] = True
            sum_time += score_table[i][0]
            last_score = score_table[i][1]
            sum_score += last_score
            DFS(i+1,sum_score,sum_time,last_score)
            check[i] = False
            sum_time -= score_table[i][0]
            sum_score -= last_score


DFS(0,0,0,0)
print(max_score)