def solution(n, t, m, timetable): 
    answer = 0 
    crewTime = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    crewTime.sort()
    busTime = [9*60 + t*i for i in range(n)] 
    idx = 0
    for bus_stop in busTime: 
        cnt = 0 
        while cnt < m and idx < len(crewTime) and crewTime[idx] <= bus_stop: 
            idx += 1 
            cnt += 1 
        if cnt < m: 
            answer = bus_stop
        else: 
            answer = crewTime[idx - 1] - 1 
    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)

print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))