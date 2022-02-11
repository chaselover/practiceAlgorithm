
def check_winner(hit):
    lion_cnt = 0
    apeach_cnt = 0
    for i in range(11):
        if hit[i] > apeach_info[i]:
            lion_cnt += 10-i
        elif apeach_info[i]:
            apeach_cnt += 10-i
    return lion_cnt - apeach_cnt



def dfs(cnt,target,hit):
    global max_gap,answer
    if cnt==target:
        gap = check_winner(hit)
        if max_gap < gap:
            max_gap = gap
            answer = hit[:]
        return
    for i in range(11):
        hit[i] += 1
        gap = check_winner(hit)
        dfs(cnt+1,target,hit)
        hit[i] -= 1


def solution(n, info):
    global max_gap,apeach_info,answer
    # 가장 큰 점수차로 라이언이 이겨야함.
    # 총 n발.
    # info는 10점부터 0점까지 맞춘 숫자의 counter
    # 라이언이 이길수 없는(지거나 비기면 [-1]리턴.)
    # 가장 큰 점수차를 만들 방법이 여러가지 안경우 낮은 점수를 더 많이 맞춘 경우를 return
    apeach_info = info
    lion_info = [0,0,0,0,0,0,0,0,0,0,0]
    max_gap = -float('inf')
    answer = []
    dfs(0,n,lion_info)
    return answer if max_gap > 0 else [-1]


print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))