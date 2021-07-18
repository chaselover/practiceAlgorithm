def solution(progresses, speeds):
    N = len(speeds)
    dp = [0]*N
    count=0
    answer = []
    
    for i in range(N):
        dp[i] = ((100 - progresses[i])//speeds[i])
        if((100 - progresses[i])%speeds[i]) != 0:
            dp[i]+=1
            
    max = dp[0]
    for i in range(N):
        if max>=dp[i]:
            count+=1
        else:
            answer.append(count)
            count=1
            max=dp[i]
    answer.append(count)
    return answer

# 다른사람 풀이
# -((p-100)//s)는 올림한 양수
# zip은 동일개수 자료형을 튜플로 묶어주는 함수
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]