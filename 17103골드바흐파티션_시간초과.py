import sys
input = sys.stdin.readline

def isPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

T = int(input())


for test in range(T):
    N = int(input())
    cnt = 0
    for i in range(2, int(N/2)+1):
        if isPrime(i) and isPrime(N-i):
            cnt+=1
    print(cnt)
                