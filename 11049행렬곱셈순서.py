import sys
input = sys.stdin.readline


N = int(input())
matrix = [list(map(int, input().split())) for i in range(N)]
# dp[i][j]는 i번재 행렬에서 j번째 행렬까지 곱한
dp = [[0] * N for _ in range(N)]
for i in range(1, N): #몇 번째 대각선? 0번째 대각선은 자기자신이므로 0유지.
    for j in range(0, N-i): #대각선에서 몇 번째 열?(N*N에서 반만 채우므로 대각선 번호가 끝으로 갈수록 계산해야되는 칸도 하나씩 줄어감)
        x = i+j             # 차이가0인 본인대각선 모든값 0 -> 첫 대각선 계산수 N-1 -> 두번째 대각선 계산수 N-2 .... N번째 대각선 1회. 
        if i == 1:          # x는 i번째 대각선의 j번째 열. 대각선은 한칸마다 1,1씩 증가해야하므로 j가 양쪽에 들어가 1씩 증가시켜준다.i는 표준편차의 크기.
            dp[j][x] = matrix[j][0] * matrix[j][1] * matrix[x][1]   # 계산 횟수는 가운데 낀 숫자는 1번 맨앞, 맨뒤숫자 1번씩 곱.
            continue
        
        dp[j][x] = 2**32 #최댓값을 미리 넣어줌(min연산을 위해 inf값 할당해주듯)
        #k는 A~E중 어디를 자르는가의 문제. ex ABC라면 AB,C / A,BC 
        #즉 k에따라 콤마위치가 변하고 dp[j][k]는 j부터 k행렬까지의 최소값, dp[k+1][x]는 K+1에서 x까지의 최솟값
        #뒤에 곱하는 dp는 앞행렬과 뒷행렬을 곱하는 횟수(A의 행수*자르는index인 k의 열수*마지막인자인 x의 열수)
        for k in range(j, x):           
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + matrix[j][0] * matrix[k][1] * matrix[x][1])
                
    
print(dp[0][N-1]) #맨 오른쪽 위