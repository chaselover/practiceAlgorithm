import sys
input = sys.stdin.readline
from collections import defaultdict

N, K = map(int,input().split())
A = list(map(int,input().split()))

# 200000이하 N, 같은 정수를 K개 이하 포함한 최장 연속 부분수열.
count = defaultdict(int)
max_length = 0
last_start = 0

for i in range(N):
    count[A[i]] += 1

    if count[A[i]] > K:                     # 탐색 -> A숫자 count가 K+1개 되면 lenth i-0기록 -> 
        if max_length < i- last_start:      # -> 또 나오면 max_length 비교. 최대면 최신화. 
            max_length = i- last_start
        while count[A[i]] > K:              # 처음으로 A숫자 나온 인덱스 뒤부터 재탐색 (시간초과나면 heapq나 deque)
            count[A[last_start]] -= 1       # 초기화 되는 index 앞 count 전부 초기화.
            last_start +=1
    else:
        if max_length < i+1- last_start:    # -> 수열 끝까지 가면 max_length 측정
            max_length = i+1- last_start

print(max_length)