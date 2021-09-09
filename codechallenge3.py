import sys
input = sys.stdin.readline
from math import ceil

def is_possible(target,gold,silver,g_list,s_list,w_list,t_list):
    n = len(g_list)
    need_to_move = gold + silver
    for i in range(n):
        # 편도 cnt번 왕복 가능.
        cnt = target//t_list[i]
        # 한번에 w_list[i]
        total = w_list[i]*ceil(cnt/2)
        if total > g_list[i] + s_list[i]:
            total = g_list[i] + s_list[i]
        need_to_move -= total
        if need_to_move <= 0:
            return True
    return False



def solution(a, b, g, s, w, t):
    left = 0
    right = int(2e14)
    answer = 0
    while left <= right:
        mid = (left + right)//2
        if is_possible(mid, a, b, g, s, w, t):
            right = mid-1
            answer = mid
        else:
            left = mid + 1
    return answer

print(solution(10,10,[100],[100],[7],[10]))