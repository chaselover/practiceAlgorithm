import sys
input= sys.stdin.readline

# 계속 sum에 더해가면서 진행하다가 미리 정해두었던 mid기준을 충족하면
# 그 지점 i 에서 다시 less_than_target 시작하고 group count 1부터 다시 시작. 총 M개로 나뉠때까지 진행.
# 다해서 M개 이상 되면 최솟값 탐색을 위해 왼쪽 탐색,  M개 안되면 mid늘려야하므로 오른쪽 탐색.
def get_Mgroup(target_sum):
    sum_each_group=0
    group_cnt = 1
    for i in range(N):
        sum_each_group += ball_lists[i]
        if sum_each_group > target_sum:
            sum_each_group = ball_lists[i]
            group_cnt+=1
    if group_cnt <=M:
        return True
    else:
        return False

def cut_each_points(target_sum,M,N):
    print(target_sum)
    less_than_target=0
    ball_cnt = 0
    for i in range(N):
        less_than_target += ball_lists[i]
        if less_than_target > target_sum:
            less_than_target = ball_lists[i]
            M -=1
            print(ball_cnt, end=" ")
            ball_cnt=0
        ball_cnt+=1

        if N-i ==M:
            break

    while M:
        print(ball_cnt, end=" ")
        ball_cnt=1
        M-=1


N,M = map(int,input().split())
ball_lists = list(map(int,input().split()))

# 이분 탐색. 탐색 범위는 원소의 sum영역이 될 수 있는 모든 값.
# 좌: 원소중 최대값, 우: 총합값으로 이분 탐색을 진행 target_sum을 찾음.
left_sum_limit = max(ball_lists)
right_sum_limit = sum(ball_lists)

# 좌 우 탐색할 영역 선택. 선택 갯수를 만족하면 좀 더 작게 하기위해 좌측 탐색
# M을 만족하지 못하면 mid를 크게잡아 만족시켜야 하기 때문에 우측탐색.
# 계속 반으로 나눠가며 영역 탐색.
# left가 right를 만나는 영역(최적 mid값을 찾으면 종료.)
while left_sum_limit <= right_sum_limit:
    target_sum = (left_sum_limit+right_sum_limit)//2
    if get_Mgroup(target_sum):
        right_sum_limit = target_sum -1
    else:
        left_sum_limit = target_sum+1

cut_each_points(left_sum_limit,M,N)