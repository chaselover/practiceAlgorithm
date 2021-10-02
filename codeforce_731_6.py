import sys
input = sys.stdin.readline
from collections import defaultdict

for test in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    primes = defaultdict(int)
    for i in range(n):
        tmp = a[i]
        for j in range(2, tmp + 1):
            if tmp == 1:
                break
            if not tmp % j:
                while not tmp % j:
                    tmp //= j
                primes[j] += 1
    print(primes)
    max_cnt = 0
    for prime in primes:
        if not primes[prime] == n and max_cnt < primes[prime]:
            max_cnt = primes[prime]
    print(max_cnt)