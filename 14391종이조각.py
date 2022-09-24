import itertools

# input
n, m = map(int, input().split())
x_lst = []
for _ in range(n):
    x_lst.append(list(map(int, (input()))))

# matrix 1d -> 2d convert
def to_matrix(l,m) :
    return [l[i:i+m] for i in range(0, len(l), m)]

# itertools의 product를 이용해서 비트마스크 제너레이터 만들기 
# e.g) (0,0,0,0), (0,0,0,1) ... (1,1,1,1)
a = itertools.product([0, 1], repeat=n*m)
ans = 0

# 가로부터 합계를 구해주고 세로 합계 구해줘서 더함
for x in a:
    bit_mask = to_matrix(x, m)
    sumh = 0

    for i in range(n):
        hori = 0
        for j in range(m):
            if bit_mask[i][j] == 0:
                hori = 10 * hori + x_lst[i][j]
            if bit_mask[i][j] == 1 or j == m - 1:
                sumh = sumh + hori
                hori = 0

    sumv = 0

    for j in range(m):
        vert = 0
        for i in range(n):
            if bit_mask[i][j] == 1:
                vert = 10 * vert + x_lst[i][j]
            if bit_mask[i][j] == 0 or i == n - 1:
                sumv = sumv + vert
                vert = 0

    sum_all = sumh + sumv

    ans = max(ans, sum_all)

print(ans)