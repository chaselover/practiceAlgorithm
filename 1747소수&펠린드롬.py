import sys
input = sys.stdin.readline


N = int(input())
primes = [True] * 2000000
primes[0] = primes[1] = False
for i in range(2,1001):
    if primes[i]:
        for j in range(i+i,2000000,i):
            primes[j] = False
for i in range(N,2000000):
    if primes[i]:
        c_i = str(i)
        if c_i == c_i[::-1]:
            print(i)
            break