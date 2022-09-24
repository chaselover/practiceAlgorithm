import sys
sys.stdin = open('input.txt')


def special_sort(length, arr):
    arr.sort()
    max_idx = length-1
    min_idx = 0
    special_arr = []
    # 정렬한 배열의 양끝에서부터 하나씩 특별한 배열로 삽입합니다.
    # 양끝이 만나면 종료합니다.
    while min_idx <= max_idx:
        special_arr.append(arr[max_idx])
        special_arr.append(arr[min_idx])
        max_idx -= 1
        min_idx += 1
    return special_arr[:10]


for test in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = special_sort(N, arr)
    print(f'#{test}', end=' ')
    print(*answer)


import sys
from collections import deque
sys.stdin = open('input.txt')


def special_sort(arr):
    arr.sort()
    queue = deque([*arr])
    special_arr = []
    while queue:
        special_arr.append(queue.pop())
        special_arr.append(queue.popleft())
    return special_arr[:10]


for test in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = special_sort(arr)
    print(f'#{test}', end=' ')
    print(*answer)

import sys
from heapq import heappop,heapify
sys.stdin = open('input.txt')


def special_sort(arr):
    length = len(arr)
    minus_arr = list(map(lambda x: -x, arr))
    heapify(arr)
    heapify(minus_arr)
    special_arr = []
    cnt = 0
    while cnt != length:
        special_arr.append(-heappop(minus_arr))
        cnt += 1
        if cnt == length:
            break
        special_arr.append(heappop(arr))
        cnt += 1
    return special_arr[:10]


for test in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = special_sort(arr)
    print(f'#{test}', end=' ')
    print(*answer)
