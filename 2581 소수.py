import sys
input = sys.stdin.readline


def che():
    nums = [True]*(N+1)
    nums[0]=nums[1]=False
    primes = []
    for i in range(2,int(N**0.5)+1):
        if nums[i]:
            for j in range(i+i, N+1, i):
                nums[j] = False
    return [i for i in range(M,N+1) if nums[i]]

M = int(input())
N = int(input())
arr = che()
if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)
