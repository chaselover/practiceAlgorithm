import sys
input = sys.stdin.readline
from heapq import heappush,heappop

# key값 관리를 통해 어떤 수를 삽입하면 True 삭제하면 그 키값을 False로 바꿔서 반대편 힙에서 맨앞에 삭제한 수가 나왔을때 미리 
#  삭제를 해주고 삭제연산을 시작한다.
T = int(input())
for test in range(T):
    k = int(input())
    max_heap=[]
    min_heap=[]
    visited = [False] * 1000001
    for i in range(k):
        command,n = input().split()
        n=int(n)
        if command=='D':
            if n==1:
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heappop(min_heap)
        else:
            heappush(max_heap,(-n,i))
            heappush(min_heap,(n,i))
            visited[i] = True
    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heappop(min_heap)

    if max_heap and min_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print("EMPTY")
