
from collections import deque

def check(x,y):
    if sum(x) != sum(y):
        return False
    queue = deque()
    l_y = len(y)
    l_x = len(x)
    for i in range(l_x):
        for j in range(l_y):
            if x[i]==y[j]:
                x[i] = 0
                y[j] = 0
    n_x = [num for num in x if num]
    n_y = [num for num in y if num]
    l_y = len(n_y)
    l_x = len(n_x)
    y_check = [False for _ in range(l_y)]
    for i in range(l_x):
        queue.append([1<<i,n_x[i]])
    while queue:
        check_x, sum_n = queue.popleft()
        for i in range(l_x):
            if not check_x & (1<<i):
                next_num = n_x[i]
                tmp = sum_n + next_num
                for j in range(l_y):
                    if not y_check[j] and tmp == n_y[j]:
                        y_check[j] = True
                        break
                else:
                    check_x |= (1<<i)
                    queue.append([check_x,tmp])
    if all(y_check):
        return True
    else:
        return False




def solution(p, q):
    n = len(p)
    answer = []
    for case in range(n):
        answer.append(check(p[case],q[case]))
        print()
    return answer


print(solution([[5,3,2,2,1]],[[7,2,4]]))