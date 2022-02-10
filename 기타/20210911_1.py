# 브루스포스(n3)으로 풀림.
# 이전에 들고있던 sum값에 새로 들어오는 애들만 정리해주는 방식.(n2)
# 투포인터 2번 돌리는 방법. 합이 k이하인 연속 부분수열의 갯수를 k-1이하인 연속 부분수열의 갯수에서 빼면됨.

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
