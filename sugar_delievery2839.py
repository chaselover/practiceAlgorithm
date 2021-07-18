"""
N명의 사람들 줄서있음.
i번 사람이 인출하는데 Pi분 걸림.
"""
N = int(input())
P = list(map(int,input().split()))

mintime = sorted(P)
answer = 0
for i in range(N):
    answer += (N-i)*mintime[i]

print(answer)