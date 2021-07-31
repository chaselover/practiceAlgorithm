import sys
input = sys.stdin.readline

N, K = map(int, input().split())

answer = 0
while bin(N).count('1') > K:
    plus = 2 ** (N&~N)
    answer += plus
    N += plus
print(answer)