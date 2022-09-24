import sys
input = sys.stdin.readline

def find_prime():
    n = 10000000
    a = [True]*(n+1)
    m = int(10000000**0.5)
    for i in range(2,m+1):
        if a[i]==True:
            for j in range(i+i,n+1,i):
                a[j] = False
    return [i for i in range(2,n+1) if a[i]==True]


for test in range(1,int(input())+1):
    m = int(input())
    arr = list(map(int,input().split()))
    prime_common = [set() for _ in range(m)]
    primes = find_prime()
    len_p = len(primes)
    for i in range(m):
        n = arr[i]
        window_sum = 0
        window_start = 0
        for window_end in range(len_p):
            window_sum += primes[window_end]
            if window_end >= (n-1):
                if window_sum in primes:
                    prime_common[i].add(window_sum)
                window_start += 1
                window_sum -= primes[window_start]
    print(prime_common)