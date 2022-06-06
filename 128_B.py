import sys
input = sys.stdin.readline


def isCheck():
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "R":
                for i2 in range(i + 1, n):
                    for j2 in range(j):
                        if matrix[i2][j2] == "R":
                            return False
                return True
    return False


for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = [input().rstrip() for _ in range(n)]
    print("YES" if isCheck() else "NO")

