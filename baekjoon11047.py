import sys

N = int(input())
roof = []

for _ in range(N):
    roof.append(int(input()))

roof = sorted(roof)
answer = []

for i in range(1,N+1):
    if roof[-i]*i >= answer:
        answer = roof[-i]*i

print(answer)