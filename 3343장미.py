import sys
input = sys.stdin.readline
from collections import deque

def buy_flower(optimal_cost):
    queue = deque()
    start_price = 0
    flower = 0
    queue.append([start_price,flower])
    while queue:
        cur_price,flower = queue.popleft()
        for flo_cnt,flo_cost in ((A,B),(C,D)):
            if cur_price + flo_cost <= optimal_cost:
                queue.append([cur_price+flo_cost,flower+flo_cnt])
                if flower+flo_cnt>=N:
                    return True



N,A,B,C,D = map(int,input().split())

start = 1
end = int(1e18)
answer = 0
while start <= end:
    mid = (start+end)//2
    if buy_flower(mid):
        end = mid-1
        answer = mid
    else:
        start = mid +1

print(answer)