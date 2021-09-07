import sys
input = sys.stdin.readline
import heapq

n = int(input())
road_info = []
for _ in range(n):
    road = list(map(int, input().split()))
    road_info.append(road)

d = int(input())
roads = []
for road in road_info:
    house, office = road
    if abs(house - office) <= d:
        road = sorted(road)
        roads.append(road)
roads.sort(key=lambda x:x[1])

answer = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))

print(answer)

# 다른풀이
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def solution(n):
    lst = [sorted(list(map(int, input().split()))) for i in range(n)]
    lst.sort(key=lambda x: x[1])
    d = int(input())
    result = -1
    heap = []
    for s, e in lst:
        lim = e - d
        if s >= lim:
            heappush(heap, s)
        while heap and heap[0] < lim:
            heappop(heap)
        result = max(result, len(heap))
    print(result)

if __name__ == '__main__':
    solution(int(input()))