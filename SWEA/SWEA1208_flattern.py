import sys
input = sys.stdin.readline
from heapq import heapify, heappop,heappush

for test in range(1,11):
    dump = int(input())
    boxes = list(map(int,input().split()))
    minus_boxes = list(map(lambda x:-x,boxes))
    heapify(boxes)
    heapify(minus_boxes)

    for _ in range(dump):
        highest_point = -heappop(minus_boxes)
        lowest_point = heappop(boxes)
        heappush(minus_boxes,-(highest_point-1))
        heappush(boxes,lowest_point+1)

    print(f'#{test} {-heappop(minus_boxes)-heappop(boxes)}')