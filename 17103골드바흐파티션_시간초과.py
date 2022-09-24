import sys
input = sys.stdin.readline

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

T = int(input())

for test in range(T):
    N = int(input())
    if N==0:
        break
    else:
        cnt=0
        for i in range(1, int(N/2)+1):
            if isPrime(i) and isPrime(N-i):
                cnt+=1
        print(cnt)
                