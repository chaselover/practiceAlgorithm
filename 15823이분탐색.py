import sys
input = sys.stdin.readline
from collections import defaultdict


def is_Possible(pack_size):
    visited = defaultdict(int)
    cnt = 0
    left = 0
    for right in range(N+1):
        visited[cards[right]] += 1
        while visited[cards[right]] > 1:
            visited[cards[left]] -= 1
            left += 1
        if right-left+1 == pack_size:
            cnt += 1
            while left != right:
                visited[cards[left]] -= 1
                left += 1
    if cnt >= M:
        return True
    return False



N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.append(cards[-1])
left = 1
right = N
answer = 0
while left <= right:
    mid = (left+right)//2
    if is_Possible(mid):
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
print(answer)


def my_bisect(lo, hi):
    answer = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = count_m(mid)
        if cnt >= M:
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return answer

# # 길이가 m인 윈도우(팩) 수 // 슬라이딩 윈도우가 아니라 윈도우 실패함수.를 dict로 구현.
# def count_m(mid):
#     cnt = 0
#     move = 0

#     while mid + move <= N:
#         # 같은 거 중복할때까지 전진
#         visited = dict()
#         for i in range(move, move + mid):
#             # 중복시 다음 스타트 지점
#             # 전에 나온놈 인덱스 저장하고 중복시 여기인덱스 바로 뒤로 점프해 다시탐색(실패함수.) 
#             if cards[i] not in visited:
#                 visited[cards[i]] = i
#             else:
#                 move = visited[cards[i]] + 1
#                 break
#         # 반복문 후 else = 반복문 종료시 1회 실행
#         else:
#             cnt = cnt + 1
#             move = move + mid

#     return cnt


# N, M = map(int, input().split())
# cards = list(map(int, input().split()))

# # 카드팩 최소, 최대 크기
# lo = 1
# hi = N//M
# print(my_bisect(lo, hi))