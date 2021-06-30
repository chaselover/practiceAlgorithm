import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]
electric = list(input())
P = int(input()) - electric.count("Y")
dp=[[0,0]] * N
cnt = 0

if electric.count("Y") == 0:
    print(-1)
elif electric.count("Y") > P:
    print(0)

while P != cnt:
    for i in range(N):
        if electric[i] == "Y":
            for j in range(N):
                if i != j and dp[j][0] == cnt :
                    dp[j] = [cnt+1, dp[j][1] + cost[i][j]]
                    print(dp)


    # 일단 Y인것들 dp에 다 초기화.
    # 0이 아닌 것들 중에서 똑같이 진행.
    # cnt이용 P만큼 켜졌을때 종료. 가장 작은 dp로 채택.

    for i in range(N):
        if dp[i][1] != 0:
            electric[i] = "Y"
    
    cnt+=1

ans_list = []
for i in range(N):
    if dp[i][0] == P:
        ans_list.append(dp[i][1])

if not ans_list:
    print(-1)
else:
    print(min(ans_list))
