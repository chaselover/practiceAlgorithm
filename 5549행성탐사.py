import sys
input = sys.stdin.readline

# 세로 M 가로 M
M,N = map(int,input().split())
K = int(input())
maps = [list(input().rstrip()) for _ in range(M)]

dp = [[[0,0,0] for _ in range(N)] for _ in range(M)]

# 정글 J 바다 O 얼음 I
for i in range(M):
    for j in range(N):
        if i and j:
            for k in range(3):
                dp[i][j][k] = dp[i][j-1][k]+dp[i-1][j][k]-dp[i-1][j-1][k]
            if maps[i][j] =='J':
                dp[i][j][0] += 1
            elif maps[i][j] =='O':
                dp[i][j][1] += 1
            elif maps[i][j] == 'I':
                dp[i][j][2] += 1
        elif not i and j:
            for k in range(3):
                dp[i][j][k] = dp[i][j-1][k]
            if maps[i][j] =='J':
                dp[i][j][0] += 1
            elif maps[i][j] =='O':
                dp[i][j][1] += 1
            elif maps[i][j] == 'I':
                dp[i][j][2] += 1
        elif i and not j:
            for k in range(3):
                dp[i][j][k] = dp[i-1][j][k]
            if maps[i][j] =='J':
                dp[i][j][0] +=1
            elif maps[i][j] =='O':
                dp[i][j][1] +=1
            elif maps[i][j] == 'I':
                dp[i][j][2] +=1
        elif not i and not j:
            if maps[i][j] =='J':
                dp[i][j][0]=1
            elif maps[i][j] =='O':
                dp[i][j][1]=1
            elif maps[i][j] == 'I':
                dp[i][j][2]=1

# 출력범위 조절.
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    answer = []
    if x1 !=1 and y1 != 1:
        for k in range(3):
            answer.append(dp[x2-1][y2-1][k] - dp[x1-2][y2-1][k] - dp[x2-1][y1-2][k] + dp[x1-2][y1-2][k])
    elif x1 !=1 and y1==1:
        for k in range(3):
            answer.append(dp[x2-1][y2-1][k] - dp[x1-2][y2-1][k])
    elif x1 ==1 and y1!=1:
        for k in range(3):
            answer.append(dp[x2-1][y2-1][k] - dp[x2-1][y1-2][k])
    elif x1==1 and y1==1:
        for k in range(3):
            answer.append(dp[x2-1][y2-1][k])
    print(*answer)