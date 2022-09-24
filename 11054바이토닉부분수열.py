N = int(input())
A = [0] + list(map(int, input().split()))
LDS = [1]*(N+1)
LIS = [1]*(N+1)
Bi = []



for i in range(1,N+1):
    for j in range(1,i):
        if A[i]>A[j] and LIS[i]<=LIS[j]:
            LIS[i] = LIS[j] + 1
        if A[-i]>A[-j] and LDS[-i]<=LDS[-j]:
            LDS[-i] = LDS[-j] + 1

for i in range(1,N+1):
    Bi.append(LIS[i]+LDS[i]-1)

print(max(Bi))
