import sys
input = sys.stdin.readline
from heapq import heappop,heappush

def topological_sort():
    heap=[]
    for i in range(1,N+1):
        if not level[i]:
            heappush(heap,i)
    while heap:
        cur_solve = heappop(heap)
        answer.append(cur_solve)
        for next_solve in ordered[cur_solve]:
            level[next_solve] -=1
            if not level[next_solve]:
                heappush(heap,next_solve)

# 문제는 모두 풀어야한다. 먼저푸는게 좋은 문제는 먼저 푼느걸 반드시 먼저 ㅍ루어야한다.
# 가능하면 쉬운문제부터 풀어야한다.(앞번호부터)

N,M = map(int,input().split())
ordered = {i:[] for i in range(1,N+1)}
level = {i:0 for i in range(1,N+1)}
answer = []
for _ in range(M):
    first,second = map(int,input().split())
    ordered[first] += [second]
    level[second] +=1

topological_sort()

print(*answer)