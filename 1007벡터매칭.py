import math

ax = []
ay = []
c = [False] * 21

com = [2147483647.0]

def dfs(count, index, N):
    if (count == N / 2):
        x = 0
        y = 0
        for i in range(0, N):
            if c[i]:
                x = x - ax[i]
                y = y - ay[i]
            else:
                x = x + ax[i]
                y = y + ay[i]

        com[0] = min(com[0], math.sqrt(x * x + y * y))
        return

    if (index == N):
        return

    dfs(count, index + 1, N)
    c[index] = True
    dfs(count+1, index + 1, N)
    c[index] = False

def solution():
    ax.clear()
    ay.clear()
    c = [False] * 21
    com[0] = 2147483647.0

    N = int(input())
    for i in range(N):
        x, y = map(int, input().split(' '))
        ax.append(x)
        ay.append(y)
    dfs(0, 0, N)

    print(round(com[0], 6))

T = int(input())

for i in range(T):
    solution()