import sys
input = sys.stdin.readline

N, K = map(int, input().split())
min_gap = K * (K + 1) // 2
if min_gap > N:
    print(-1)
    exit()
answer = K - 1 if not (N - min_gap) % K else K
print(answer)