def bitmask():
    global maxAns
    # 비트마스크로 2^(N*M)의 경우의 수를 따져본다
    for i in range(1 << n * m):
        total = 0
        # 가로 합 계산
        for row in range(n):
            rowsum = 0
            for col in range(m):
                # idx 는 이차원 배열을 일렬로 늘렸을때의 인덱스가 어디인지 의미(몇열 몇번째 행인가?)
                # (col 즉 idx는 오른쪽으로 늘어나며 검사.)
                idx = row * m + col
                # i번째 경우의 수에서 idx번째 요소가 있는가? 있으면 더한다 즉 이어져있는 수면 더한다.(1이면 가로로 더하겠다는 의미)
                if i & (1 << idx) != 0:
                    rowsum = rowsum * 10 + arr[row][col]
                # 세로일때 앞에서 나온 수를 total에 더하고 rowsum 초기화
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum

        # 세로 합 계산
        for col in range(m):
            colsum = 0
            for row in range(n):
                # idx 는 이차원 배열을 일렬로 늘렸을때의 인덱스가 어디인지 의미(
                # row가 증가하는 방향 즉 위에서 아래로 한칸씩 늘려가며 0이 나올때까지는 10의 자릿수 맞춰주고 0나오면 자릿수 초기화)
                idx = row * m + col
                # 세로일때(0이면 세로로 더하겠다는 의미) 이전에 나온 숫자를 왼쪽으로 한칸씩 밀며 1의자릿수로 들어감.
                if i & (1 << idx) == 0:
                    colsum = colsum * 10 + arr[row][col]
                # 가로일때 앞에서 나온 수를 total에 더하고 colsum 초기화
                else:
                    total += colsum
                    colsum = 0
            total += colsum
        maxAns = max(maxAns, total)


# 일단 브루트 포스임은 자명. 어떻게 전수조사할것인가?
n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

maxAns = 0
bitmask()
print(maxAns)
​
