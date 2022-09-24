for tc in range(1, int(input())+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
 
    row = 0
    col = -1
    cnt = 1
    trans = 1
    while N:
        # 가로
        for _ in range(N):
            col += trans
            arr[row][col] = cnt
            cnt += 1
        N -= 1
        # 세로
        for _ in range(N):
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1
    print('#{}'.format(tc))
    for line in arr:
        for i in line:
            print(i, end=' ')
        print()