

def solution(enter, leave):
    n = len(enter)
    answer = [0] * (n+1)
    enter_idx = 0
    leave_idx = 0
    room = set()
    while leave_idx < n:
        if leave[leave_idx] in room:
            room.discard(leave[leave_idx])
            leave_idx += 1
            continue
        if enter[enter_idx] not in room:
            for man in room:
                answer[man] += 1
            answer[enter[enter_idx]] = len(room)
            room.add(enter[enter_idx])
            enter_idx += 1
    return answer[1:]

print(solution([1,3,2],	[1,2,3]))


from collections import defaultdict

def solution(enter, leave):
    n = len(enter)
    answer = [0] * (n+1)
    enter_idx = 0
    leave_idx = 0
    room = defaultdict(set)
    check = {i: False for i in range(1, n+1)}
    while leave_idx < n:
        if check[enter[enter_idx]]:
            enter_idx += 1
            continue
        if enter[enter_idx] == leave[leave_idx]:
            if enter[enter_idx] not in room:
                for man in room:
                    room[man].add(enter[enter_idx])
                answer[enter[enter_idx]] += len(room)
                check[enter[enter_idx]] = True
            else:
                answer[enter[enter_idx]] += len(room[enter[enter_idx]])
                check[enter[enter_idx]] = True
                del(room[enter[enter_idx]])
            enter_idx = 0
            leave_idx += 1
        else:
            room[enter[enter_idx]]
            for man in room:
                if not enter[enter_idx] == man:
                    room[man].add(enter[enter_idx])
                    room[enter[enter_idx]].add(man)      
            enter_idx += 1
    return answer[1:]

# print(solution([1,3,2],	[1,2,3]))