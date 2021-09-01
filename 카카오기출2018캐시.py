from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    total_cost = 0
    for city in cities:
        lo_city = city.lower()
        if len(cache) == cacheSize:
            if lo_city not in cache:
                cache.popleft()
                cache.append(lo_city)
                total_cost += 5
            else:
                cache.append(cache.pop(cache.index(lo_city)))
                total_cost += 1
    return total_cost


print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))