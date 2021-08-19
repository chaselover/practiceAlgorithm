import sys
input = sys.stdin.readline

N = int(input())
works =  [list(map(int, input().split())) for _ in range(N)]
works = sorted(works,key = lambda x: x[1])
total_time = 0
min_rest = float('inf')
for time, limit in works:
    total_time += time
    min_rest = min(min_rest, limit-total_time)
    if limit < total_time:
        print(-1)
        exit()
print(min_rest)