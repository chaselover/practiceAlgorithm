from typing import List

def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for x, y in fires:
                x -= 1
                y -= 1
                dist = max(abs(i - x), abs(j - y))
                if dist == 0:
                    answer[i][j] -= 1
                if m >= dist:
                    answer[i][j] += m - dist + 1
            for x, y in ices:
                x -= 1
                y -= 1
                dist = abs(i-x) + abs(j-y)
                if dist == 0:
                    answer[i][j] += 1
                if m >= dist:
                    answer[i][j] -= (m - dist + 1)
    return answer




print(solution(3, 2, [[1, 1]], [[3, 3]]))