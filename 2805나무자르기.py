import sys
input = sys.stdin.readline

def isPossible(mid):
    M_cnt = 0
    for i in range(N):
        if tree[i] - mid > 0:
            M_cnt += tree[i]-mid
    if M_cnt >=M:
        return True
    else:
        return False



# 나무M미터가 필요.
# 높이 H지정하면 한줄 나무 모두 절단.
#  잘린건 상근이가 들고감.
# 목표 M미터만큼.
# H의 최댓값 구하라.
N,M = map(int,input().split())
tree = list(map(int,input().split()))

# 최소 m을 가져가는 h를 이분탐색 해보자
left = 0
right = max(tree)
while left <= right:
    mid = (left+right)//2
    if isPossible(mid):
        left = mid+1
        H = mid
    else:
        right = mid-1

print(H)