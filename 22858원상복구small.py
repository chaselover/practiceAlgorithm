import sys
input = sys.stdin.readline

N, K = map(int, input().split())
after_shuffle = list(map(int, input().split()))
D = list(map(int, input().split()))

for _ in range(K):
    tmp = [0]*N
    for i in range(N):
        tmp[D[i]-1] = after_shuffle[i]
    after_shuffle = tmp
print(*after_shuffle)