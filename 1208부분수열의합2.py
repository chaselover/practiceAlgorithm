from sys import stdin
from collections import defaultdict


def dfs(idx, end_idx, subtotal, direction):
    global answer

    # 종료 index에 왓을때 오른쪽에 진행되던 분기는 left 딕셔너리에 s-자기의 총합만큼의 left값이 있나 체크 후 그 숫자만큼 답에 더해주고
    #  왼쪽은 총합만큼 딕셔너리에 기록해준다.(왼쪽과 오른쪽의 합이 s가 되는 만큼 answer에 더해진다.)
    if idx == end_idx:
        if direction == "right":
            answer += left[s - subtotal]
        else:
            left[subtotal] += 1
        return
    # 결국 부분수열의 합은 각 원소에 대해 0또는 1로 가져갈것이냐 안가져갈 것이냐
    # 인덱스를 진행해가며 분기를 나눠 계산한다.
    dfs(idx + 1, end_idx, subtotal, direction)
    dfs(idx + 1, end_idx, subtotal + nums[idx], direction)


if __name__ == "__main__":
    answer = 0
    n, s = map(int, stdin.readline().split())
    nums = list(map(int, stdin.readline().split()))
    left = defaultdict(int)

    dfs(0, n//2, 0, "left")
    dfs(n//2, n, 0, "right")

    print(answer if s != 0 else answer - 1)