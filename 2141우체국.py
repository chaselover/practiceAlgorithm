import sys
input = sys.stdin.readline
from bisect import bisect_left

def cal_dist(position):
    dist = 0
    for town, population in arr:
        dist += abs(position-town)*population
    return dist


N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
left = -1000000000
right = 1000000000
answer = 0
while left <= right:
    mid = (left+right)//2
    if cal_dist(mid) < cal_dist(mid+1):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
arr.sort()
close_town_idx = bisect_left(arr,(answer,0))
if cal_dist(arr[close_town_idx-1][0]) <= cal_dist(arr[close_town_idx][0]):
    answer = close_town_idx-1
else:
    answer = close_town_idx
print(arr[answer][0])