import sys
input = sys.stdin.readline
 
N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()
answer = 0
left = right = 0
 
for start, end in lines:
    if not answer:
        answer = abs(end - start)
        left = start
        right = end
        continue
    
    # 여기가 스위핑문. 조건에서 벗어나는 라인은 조사 x
    if left <= start and right >= end:
        continue
    
    answer += abs(end - start)
    if right > start:
        answer -= abs(right - start)
    left = start
    right = end
 
print(answer)