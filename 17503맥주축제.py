import sys
from heapq import heappop,heappush
input = sys.stdin.readline

# N일 K종류 맥주 무료 제공
# 하루 맥주 1병 전에 받은 종류 못받음.
# 맥주 N개의 선호도 합 M이상.
# 조합 K 종류 맥주 중 N개 추출 합이 M이상되는.
# 도수 낮은거 순으로 먹음.
N, M, K = map(int, input().split())
beers = [list(map(int, input().split())) for _ in range(K)]
beers2 = sorted(beers,key=lambda x: (x[1],x[0]))
heap = []
flav_p = 0
cnt =0
left = 0
for beer in beers2:
    flav_p += beer[0]
    heappush(heap,beer[0])
    if len(heap) == N:
        if flav_p >=M:
            answer = beer[1]
            break
        else:
            flav_p -= heappop(heap)
else:
    print(-1)
    exit()
print(answer)