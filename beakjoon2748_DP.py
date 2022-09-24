



n = int(input())

T = [0]
P = [0]
dp = [0]
for _ in range(n):
    t,p = map(int, input().split())
    T.append(t)
    P.append(p)
    dp.append(p)

dp.append(0) #맨뒤시작 누적p는 0으로 설정.(dp[n]=0으로 설정된것.)

for i in range(n,0,-1):
    if T[i]+i>n: #t[i]값(소요일자) + i(날짜) 의 합이 d-day를 넘으면 선택하지않음. 
        dp[i] = dp[i+1] #날짜 넘어가면 선택안하고 1더한오른쪽값(이전값을 가져옴(역순이기때문.))
    else:  #선택이 가능하면
        dp[i] = max(dp[i+1],P[i]+dp[i+T[i]]) #나를 선택하지 않는 값과 나를 선택(p + dp[내위치+t[i]즉 내 위치를 선택했을때 도착하는 다음 노드의dp누적값]중에 더 큰것을 선택한다.)
        # 역산하면서 선택하면 전에 선택한 노드의dp값을 계승해 더하는 식으로 각 노드의 dp값을 계산.
    
    
print(dp)