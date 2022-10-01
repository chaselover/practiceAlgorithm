from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    min_dist = abs(r-x) + abs(c-y)
    if min_dist > k or (k - min_dist) & 1:
        return 'impossible'
    answer = ''
    if r > x:
        answer += 'd' * (r - x)
        k -= (r - x)
    if c < y:
        answer += 'l' * (y - c)
        k -= (y - c)
    if c > y:
        answer += 'r' * (c - y)
        k -= (c - y)
    if r < x:
        answer += 'u' * (x - r)
        k -= (x - r)
    if k:
        for idx, char in enumerate(answer):
            if char == 'u':
                if idx == 0:
                    if x == n - 1:
                        answer = answer[:1] + 'du' * (k // 2) + answer[1:]
                    else:
                        answer = 'du' * (k // 2) + answer
                else:
                    if x == n - 1:
                        if y == 0:
                            answer = answer[:1] + 'lr' * (k // 2) + answer[1:]
                    else:
                        answer = 'du' * (k // 2) + answer[idx:]
                
            
        
    return answer

print(solution(3, 4, 2, 3, 3, 1, 5))