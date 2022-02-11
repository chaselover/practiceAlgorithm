
def solution(cacheSize, cities):
    cache = []
    total_cost = 0
    for city in cities:
        lo_city = city.lower()
        if lo_city not in cache:
            cache.append(lo_city)
            total_cost += 5
            if len(cache) > cacheSize:
                cache.pop(0)
        else:
            cache.append(cache.pop(cache.index(lo_city)))
            total_cost += 1
    return total_cost

# 남의 풀이
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time



print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))