def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True



while 1:
    N = int(input())
    if N==0:
        break
    else:
        for i in range(1, N+1):
            if isPrime(i):
                A = N-i
                if isPrime(A):
                    print(f'{N} = {i} + {A}')
                    break
                