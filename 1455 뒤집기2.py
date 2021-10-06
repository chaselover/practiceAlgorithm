import sys
input = sys.stdin.readline

def xor(a, b):
    for row in range(a + 1):
        for col in range(b + 1):
            matrix[row][col] ^= 1


n, m = map(int, input().split())
matrix = [list(map(int, list(input().rstrip()))) for __ in range(n)]
cnt = 0
for row in range(n - 1, -1, -1):
    for col in range(m - 1, -1, -1):
        if matrix[row][col]:
            cnt += 1
            xor(row, col)
print(cnt)