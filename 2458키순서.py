import sys
input = sys.stdin.readline

N, M = map(int, input().split())
knowing_tall = [[0 for _ in range(N)] for _ in range(N)]

# 플로이드 워셜은 인접행렬을 쓴다.
for i in range(M):
    high, low = map(int, input().split())
    knowing_tall[high-1][low-1] =1

# 플로이드 워셜의 핵심은 matrix[a][b]랑 matrix[b][a]의 차이를 잘 생각하고 그래프를 설계.
for k in range(N):
    for i in range(N):
        for j in range(N):
            # 내가 아는애랑 키차이 알고 걔가 다른애랑 키차이 알면 나도 걔랑 암.
            if knowing_tall[i][k] +knowing_tall[k][j]  ==2:
                knowing_tall[i][j] =1

know_cnt =[0 for _ in range(N)]
for i in range(N):
    for j in range(N):
        if knowing_tall[i][j] ==1:
            know_cnt[i] +=1
            know_cnt[j] +=1

print(know_cnt.count(N-1))