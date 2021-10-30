from collections import defaultdict

def solution(id_list, k):
    total = defaultdict(int)
    for day in id_list:
        check = set()
        for each in day.split():
            check.add(each)
        for num in check:
            if total[num] < k:
                total[num] += 1
    answer = 0
    for each in total.values():
        answer += each
    return answer