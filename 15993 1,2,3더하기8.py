from sys import stdin


if __name__ == '__main__':
    MAX, ODD, EVEN = 100001, 0, 1
    divisor = 1000000009
    dp = [[0] * 100001 for _ in range(2)]

    dp[ODD][1] = 1
    dp[ODD][2], dp[EVEN][2] = 1, 1
    dp[ODD][3], dp[EVEN][3] = 2, 2

    for i in range(4, MAX):
        dp[ODD][i] = \
            (dp[EVEN][i - 1] + dp[EVEN][i - 2] + dp[EVEN][i - 3]) % divisor
        dp[EVEN][i] = \
            (dp[ODD][i - 1] + dp[ODD][i - 2] + dp[ODD][i - 3]) % divisor

    t = int(stdin.readline())

    for _ in range(t):
        n = int(stdin.readline())
        print(dp[ODD][n], dp[EVEN][n])