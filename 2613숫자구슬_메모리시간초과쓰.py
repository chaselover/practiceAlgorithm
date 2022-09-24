import sys
input= sys.stdin.readline
from itertools import combinations

# N-1개의 사이에서 M-1개의 작대기를 뽑는 조합.
# 각 max값중 최댓값과 slice한 작대기 위치 패킹해 저장.
# 저장된 max값 정렬 후 맨앞에있는 배열 출력.

N,M = map(int,input().split())
ball_lists = list(map(int,input().split()))

maxes = float('inf')
for comb in combinations(range(1,N),M-1):
    last_cut_point = 0
    max_sum = 0
    for cut_point in comb:
        if max_sum < sum(ball_lists[last_cut_point:cut_point]):
            max_sum = sum(ball_lists[last_cut_point:cut_point])
        last_cut_point = cut_point
    if max_sum < sum(ball_lists[last_cut_point:]):
        max_sum = sum(ball_lists[last_cut_point:])
    if maxes > max_sum:
        maxes = max_sum
        max_comb = comb

print(maxes)
last_cut_p = 0
for cut_p in max_comb:
    print(cut_p-last_cut_p, end=" ")
    last_cut_p = cut_p
print(N-last_cut_p)
