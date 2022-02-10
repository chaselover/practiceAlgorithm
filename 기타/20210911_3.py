from collections import deque

def choose_job(q):
    sum_priority = {i: [0,deque()] for i in range(1,101)}
    max_priority_id = 0
    for job in q:
        if check[job[4]]:
            continue
        sum_priority[job[2]][0] += job[3]
        sum_priority[job[2]][1].append(job)
        if max_priority_id < sum_priority[job[2]][0]:
            max_priority_id = job[2]

    return sum_priority[max_priority_id][1]

def solution(jobs):
    global check
    n = len(jobs)
    for i in range(n):
        jobs[i].append(i)
    time = 0
    queue = []
    answer = []
    queue.append(jobs[0])
    idx = 0
    check = [False for i in range(n)]
    while not all(check):
        # 큐를체크해 할 작업을 골라냄.
        to_do = choose_job(queue)
        # 작업을 실시함.
        now_doing = to_do[0][2]
        while to_do:
            call_time, cost, id_n, priority, cur_idx = to_do.popleft()
            if time >= call_time:
                time += cost
            else:
                time = call_time + cost
            if not answer:
                answer.append(id_n)
            elif answer and answer[-1] != id_n:
                answer.append(id_n)
            check[cur_idx] = True
            # 작업 종료 시간에따라 큐에 작업을 할당함
            flag = 0
            tmp = idx
            for i in range(tmp+1,n):
                if time >= jobs[i][0]:
                    if jobs[i][2]==now_doing:
                        to_do.append(jobs[i])
                        idx = jobs[i][4]
                    else:
                        queue.append(jobs[i])
                        idx = jobs[i][4]
                        flag = 1
                else:
                    break
            if not flag and idx+1 < n:
                queue.append(jobs[idx+1])
            
    return answer


print(solution([[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]]))