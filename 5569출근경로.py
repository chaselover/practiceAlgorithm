import sys
input = sys.stdin.readline

# 남북 w 동서도로 h개
# 남북방향 도로는 왼쪽부터 1,2,...w개 동서도로는 아래부터 1,2,.,..h개
# 서쪽 i번째에서 남북 남쪽j번째도로가 만나는 교차로는 i,j이다.
#  (1,1) (w,h) 가는방법. 방향전환은 최소2칸이상.
# 상태값(x과표, y좌표, x방향전환가능, y방향전환 가능)
w,h = map(int,input().split())
dp = [[[[0 for _ in range(2)] for _ in range(2)] for _ in range(101)] for _ in range(101)]

# 앞의 0,1은 방향전환이 가능하냐, 불가능하냐? 뒤의 0,1은 북쪽 방향,동쪽 방향 어딜 일직선으로 통과하냐?
for i in range(2,h+1):
    dp[i][1][0][0] = 1
for i in range(2,w+1):
    dp[1][i][0][1] = 1

for i in range(2,h+1):
    for j in range(2,w+1):
        # 방향전환이 가능하고 북쪽 방향을 보는 애들은 남쪽에서 쭉 온 애들이랑 남족에서 왔는데 방향전환 불가능하던 애들.
        dp[i][j][0][0] = (dp[i-1][j][0][0] + dp[i-1][j][1][0])%100000
        # 방향전환 가능하고 동쪽 보는애드은 동쪽에서 쭉왔거나 동쪽에서 왔는데 방향전환 불가능해서 쭉온애들
        dp[i][j][0][1] = (dp[i][j-1][0][1] + dp[i][j-1][1][1])%100000
        # 방향전환 불가능한데 북쪽보는 애들은 남쪽에서 올라온 애들중에 동쪽 보고 있던 애들
        dp[i][j][1][0] = (dp[i-1][j][0][1])%100000
        # 방향전환 불가능한데 동쪽보는 애들은 동쪽에서 왔는데 원래 북쪽 보던애들.
        dp[i][j][1][1] = (dp[i][j-1][0][0])%100000

print((dp[h][w][0][0] + dp[h][w][1][0] + dp[h][w][0][1] + dp[h][w][1][1])%100000)