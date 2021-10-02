from SWEA5185_이진수 import N
import sys
input = sys.stdin.readline

for test in range(int(input())):
    input()
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))
    answer = [float('inf')] * (n+1)
    for j in range(1, n):
        for i in range(k):
            answer[j] = min(answer[j], t[j] - abs(a[i] - j))
    print(*answer[1:])