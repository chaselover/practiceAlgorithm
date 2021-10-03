import sys
input = sys.stdin.readline

N, W = map(int, input().split( ))
costs = [int(input()) for __ in range(N)]
coin = 0
for i in range(1, N):
    if not coin:
        if costs[i - 1] < costs[i]:
            coin = W // costs[i - 1]
            W -= coin * costs[i - 1]
    else:
        if costs[i - 1] > costs[i]:
            W += coin * costs[i - 1]
            coin = 0
if coin: W += coin * costs[N - 1]
print(W)

