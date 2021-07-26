import sys, copy
input = sys.stdin.readline




def investigate(gap):
    global tempArr
    tempArr = copy.deepcopy(arr)
    operCount = 0

    # 인접한 수의 차이가 우리가 설정한 평균보다 크면  감소연산을 평균과 실제의 갭만큼 시킨다.
    for i in range(N - 1):
        if tempArr[i + 1] - tempArr[i] > gap:
            operCount += tempArr[i + 1] - (tempArr[i] + gap)
            tempArr[i + 1] = tempArr[i] + gap
    # 이건 뒤가 앞이 뒤보다 큰거
    for i in range(N - 1, 0, -1):
        if tempArr[i - 1] - tempArr[i] > gap:
            operCount += tempArr[i - 1] - (tempArr[i] + gap)
            tempArr[i - 1] = tempArr[i] + gap
    # 연산끝나고 총 횟수가 T보다 작으면 성공 아니면 실패
    if operCount <= T:
        return True
    return False

N, T = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = 1e9
result = []

# 성공하면 오른쪽을 쭉 당겨서 설정한 mid값을 줄이려고 해보고
# 실패하면 왼쪼을 땡겨서 mid값을 키우고 연산횟수를 줄이려고 노력해본다.
while left <= right:
    mid = (left + right) // 2
    if investigate(mid):
        result = copy.deepcopy(tempArr)
        right = mid - 1
    else:
        left = mid + 1
print(*result)