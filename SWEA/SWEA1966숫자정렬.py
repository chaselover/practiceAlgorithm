import sys
sys.stdin = open('input.txt')


# 선택정렬. 앞에서부터 최솟값을 찾아 swap 시킨다.
def sort_arr(arr):
    for i in range(N-1):
        min_value = float('inf')
        min_idx = 0
        for j in range(i,N):
            if arr[j] < min_value:
                min_value = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


for test in range(1, int(input())+1):
    N = int(input())
    init_arr = list(map(int, input().split()))
    sorted_arr = sort_arr(init_arr)
    print(f'#{test}', end=' ')
    print(*sorted_arr)


import sys
sys.stdin = open('input.txt')


# 버블정렬. 끝부터 범위를 하나씩 줄여가며 앞뒤로 스왑시킨다. 스왑이 일어나지 않으면 정렬 완료.
def sort_arr(N, arr):
    for i in range(N-2, -1, -1):
        swap = 0
        for j in range(0, i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = 1
        if not swap:
            return arr
    return arr


for test in range(1, int(input())+1):
    N = int(input())
    init_arr = list(map(int, input().split()))
    sorted_arr = sort_arr(N, init_arr)
    print(f'#{test}', end=' ')
    print(*sorted_arr)


import sys
sys.stdin = open('input.txt')


# 삽입 정렬. 순서대로 하나씩 빼서 내 앞에 있는 애들이랑 비교. 나보다 작은애 만나면 그 뒤에 삽입.
def sort_arr(N, arr):
    for i in range(1, N):
        tmp = i
        for j in range(i-1, -1, -1):
            if arr[tmp] < arr[j]:
                arr[tmp], arr[j] = arr[j], arr[tmp]
                tmp -= 1
            else:
                break
    return arr


for test in range(1, int(input())+1):
    N = int(input())
    init_arr = list(map(int, input().split()))
    sorted_arr = sort_arr(N, init_arr)
    print(f'#{test}', end=' ')
    print(*sorted_arr)


import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)


# 퀵 정렬 : 정렬기준인 pivot 을 통해 좌우 범위로 나눠 정렬하고 합치는 정렬.
def sort_arr(arr):
    length = len(arr)
    if length <= 1:
        return arr
    middle = length//2
    pivot = arr[middle]     # pivot 은 정렬되지 않는 배열의 중앙값이며 대소비교의 기준입니다.
    rest = arr[:middle] + arr[middle+1:]    # pivot 과 비교할 모집단입니다.
    left_arr = [i for i in rest if i <= pivot]      # pivot 보다 작은 수들의 집합입니다.
    right_arr = [i for i in rest if i > pivot]      # pivot 보다 큰 수들의 집합입니다.
    return sort_arr(left_arr) + [pivot] + sort_arr(right_arr)      # 정렬이 끝났으면 다시 합칩니다.


for test in range(1, int(input())+1):
    N = int(input())
    init_arr = list(map(int, input().split()))
    sorted_arr = sort_arr(init_arr)
    print(f'#{test}', end=' ')
    print(*sorted_arr)


import sys
sys.stdin = open('input.txt')


# 앞에서 부터 비교해 작은 숫자부터 새로운 배열에 병합합니다.
# 연산이 끝나면 정렬된 배열 merged 가 반환됩니다.
def merge(left, right):
    merged = []
    while left or right:
        if not left:
            merged += right
            return merged
        elif not right:
            merged += left
            return merged

        if left[0] < right[0]:
            merged += [left[0]]
            left = left[1:]
        else:
            merged += [right[0]]
            right = right[1:]
    return merged


# 병합 정렬 : 분할 정복을 이용한 정렬. 퀵정렬이 pivot을 기준으로 한다면 얘는 그냥 무지성 반갈.
# 반갈을 1개씩 남을때까지 한 다음 다시 병합하는데 맨앞부터 비교해서 작으면 앞에 놓는 식.
def sort_arr(arr):
    length = len(arr)
    if length <= 1:
        return arr
    middle = length//2
    left_arr = sort_arr(arr[:middle])
    right_arr = sort_arr(arr[middle:])
    return merge(left_arr, right_arr)


for test in range(1, int(input())+1):
    N = int(input())
    init_arr = list(map(int, input().split()))
    sorted_arr = sort_arr(init_arr)
    print(f'#{test}', end=' ')
    print(*sorted_arr)


