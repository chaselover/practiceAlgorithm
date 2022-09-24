from typing import List
from collections import defaultdict

def solution(queries: List[List[int]]):
    answer = 0
    counter = defaultdict(int)
    level = {}
    for idx, cnt in queries:
        new_cnt = counter[idx] + cnt
        if idx not in level:
            level[idx] = 1
        if new_cnt >= level[idx]:
            answer += counter[idx]
        while new_cnt > level[idx]:
            level[idx] *= 2
        counter[idx] = new_cnt
        
    return answer




print(solution([[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]))