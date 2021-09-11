from collections import defaultdict
from math import ceil
def solution(fees, records):
    count_dict = defaultdict(str)
    total_time = defaultdict(int)
    answer = []
    for record in records:
        time, car_id, command = record.split()
        if not count_dict[car_id]:
            count_dict[car_id] = time
        else:
            hour, minute = map(int, count_dict[car_id].split(':'))
            parse_start_min = hour*60 + minute
            hour, minute = map(int, time.split(':'))
            parse_end_min = hour*60 + minute
            use_time = parse_end_min - parse_start_min
            total_time[car_id] += use_time
            del(count_dict[car_id])

    for car_id in count_dict:
        hour, minute = map(int, count_dict[car_id].split(':'))
        parse_start_min = hour*60 + minute
        last_time = 23*60 + 59
        use_time = last_time - parse_start_min
        total_time[car_id] += use_time
    
    for car_id in total_time:
        if total_time[car_id] <= fees[0]:
            answer.append([int(car_id),fees[1]])
        else:
            answer.append([int(car_id), ceil((total_time[car_id] - fees[0])/fees[2])*fees[3] + fees[1]])

    answer.sort()
    answer = list(map(list, zip(*answer)))[1]

    return answer

            


print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
