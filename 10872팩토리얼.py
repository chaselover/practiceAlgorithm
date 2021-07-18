N = int(input())

ans=1
if N>1:
    for i in range(2,N+1):
        ans *= i

print(ans)