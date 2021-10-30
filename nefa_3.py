from collections import defaultdict

def solution(logs):
    answer = []
    dic = defaultdict(dict)
    for each in logs:
        man_id, problem_id, score = each.split()
        dic[man_id][problem_id] = score
    candidate = [man for man in dic if len(dic[man]) >= 5]
    answer_set = set()
    n = len(candidate)
    for i in range(n - 1):
        for j in range(i + 1, n):
            for problem in dic[candidate[i]]:
                if problem not in dic[candidate[j]]:
                    break
                if dic[candidate[i]][problem] != dic[candidate[j]][problem]:
                    break
            else:
                answer_set.add(candidate[i])
                answer_set.add(candidate[j])
    if answer_set:
        for each in answer_set:
            answer.append(each)
    else:
        answer.append("None")
    answer.sort()
    return answer