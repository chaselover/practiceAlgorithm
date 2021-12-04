import sys
n, m, b = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height = 0
ans = 1000000000000000000000000000000
for i in range(257):
    max = 0
    min = 0
    for j in range(n):
        for k in range(m):
            if table[j][k] < i:
                min += (i - table[j][k])
            else:
                max += (table[j][k] - i)
    inventory = max + b
    if inventory < min:
        continue
    time = 2 * max + min
    if time <= ans:
    # 시간이 같을 때는 높이가 높은 순으로 출력하라는 조건에 맞게
    # for i in range(257)은 항상 i가 오름차순으로 돌기 때문에
    # 시간이 같아도 최종적으로는 높이가 높은 순으로 나오게 된다
        ans = time
        height = i
print(ans, height)