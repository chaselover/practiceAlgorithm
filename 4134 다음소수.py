import sys
input = sys.stdin.readline
from math import log2


def make_ast_sieve():
    MAX = int(4e9)
    m = int(MAX**0.5)+1
    sieve = [False,False] + [True] * m
    for i in range(2,m):
        if sieve[i]:
            for j in range(i+i,m,i):
                sieve[j] = False
    return [num for num in range(2,m) if sieve[num]]


def prime_check(num):
    
    for prime in prime_nums:
        if not num%prime and num//prime > 1:
            return False
        if prime > num:
            return True
    return True


prime_nums = make_ast_sieve()

for test_case in range(int(input())):
    n = int(input())
    MAX = int(4e9)
    if n==0 or n==1:
        print(2)
        continue
    for i in range(n,MAX+int(log2(MAX))):
        if prime_check(i):
            print(i)
            break