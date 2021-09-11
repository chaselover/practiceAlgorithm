from collections import deque

def solution(student, k):
    left = 0
    one_position = deque()
    answer = 0
    student += [1]
    for right in range(len(student)):
        if student[right]:
            one_position.append(right)
        if len(one_position) > k:
            answer += (one_position[0] - left + 1)*(right - one_position[-2])
            left = one_position.popleft() + 1
    return answer
    

print(solution([0,1,0,0],1))
