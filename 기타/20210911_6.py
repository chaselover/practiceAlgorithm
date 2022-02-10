from collections import defaultdict
from bisect import bisect_left,bisect_right

def solution(records, k, date):
    parsed_recode = []
    for recode in records:
        d = int(recode[0].replace('-',''))
        parsed_recode.append((d,recode[1],recode[2]))
    start = int(date.replace('-',''))
    tmp = start + k
    end = tmp if (tmp)%100 <= 30 else (tmp//1000)*1000 + (tmp//100 + 1)*100 + start%31 + 1
    start_idx = bisect_left(start)
    end_idx = bisect_right(end)
    count_buying = defaultdict(list)
    re_buying_ration = defaultdict(list)
    for i in range(start_idx,end_idx):
        count_buying[parsed_recode[i][1]].append(parsed_recode[i][2])

    

print(solution(["2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1", "2020-02-27 uid3 pid2", "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3", "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1", "2020-03-04 uid2 pid1", "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3", "2020-03-06 uid1 pid4"],10,"2020-03-05"))