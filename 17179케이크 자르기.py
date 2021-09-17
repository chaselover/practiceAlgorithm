import sys
input = sys.stdin.readline

def is_minimum(mini):
    left = 0
    cnt = 0
    for right in cut_points:
        if right - left >= mini:
            left = right
            cnt += 1
    if cnt > k:
        return True
    return False


N, M, L = map(int, input().split())
cut_points = [int(input()) for _ in range(M)] + [L]

for _ in range(N):
    k = int(input())
    # M개의 지점 중 k개 선택. 사잇값의 최솟값이 가장 큰.
    left = 1
    right = 4000000
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if is_minimum(mid):
            left = mid + 1
            answer = max(mid,answer)
        else:
            right = mid - 1
    print(answer)