def solution(today, terms, privacies):
    answer = []
    limits = {}
    now_year, now_month, now_day = map(int, today.split('.'))
    for term in terms:
        tp, month = term.split()
        limits[tp] = int(month) * 28
    
    for idx, privacy in enumerate(privacies):
        start, tp = privacy.split()
        s_year, s_month, s_day = map(int, start.split('.'))
        if limits[tp] <= (now_year - s_year) * 28 * 12 + (now_month - s_month) * 28 + now_day - s_day:
            answer.append(idx + 1)
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))