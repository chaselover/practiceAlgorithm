import sys
input = sys.stdin.readline


N = int(input())
postOffice = [list(map(int, input().split())) for _ in range(N)]

postOffice.sort(key=lambda x: x[0])
mid = round(sum(p for _, p in postOffice)/2)

pCount = 0
for i, p in postOffice:
    pCount += p

    if pCount >= mid:
        print(i)
        break


# import sys
# input = sys.stdin.readline

# def cal_dist(position):
#     dist = 0
#     for town, population in arr:
#         dist += abs(position-town)*population
#     return dist


# N = int(input())
# arr = [tuple(map(int, input().split())) for _ in range(N)]
# left = -1000000000
# right = 1000000000
# answer = 0
# while left <= right:
#     mid = (left+right)//2
#     if cal_dist(mid) < cal_dist(mid+1):
#         right = mid - 1
#         answer = mid
#     else:
#         left = mid + 1
# print(answer)
