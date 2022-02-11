import sys
input = sys.stdin.readline

for test in range(int(input())):
    input()
    n, k = map(int, input().split())
    a = list(map(lambda x: int(x) - 1, input().split()))
    t = list(map(int, input().split()))
    answer = [float('inf')] * n
    for i in range(k):
        answer[a[i]] = t[i]
    dp_right = [0] * n
    dp_left = [0] * n
    last = float('inf')
    for i in range(n):
        last = min(last + 1, answer[i])
        dp_right[i] = last
    for i in range(n-1, -1, -1):
        last = min(last + 1, answer[i])
        dp_left[i] = last
    for i in range(n):
        print(min(dp_left[i],dp_right[i]), end=' ')