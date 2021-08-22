# 페르마의 소정리.
# p가 소수이고 a가 p의 배수가 아닐 경우(서로소일경우)a^(p-1) = 1 (mod p)
from sys import stdin, stdout


def pow(n, k):
    if k == 1:
        return n
    pow_half = pow(n, k//2)
    if k % 2 == 0:
        return (pow_half ** 2) % MOD
    else:
        return (pow_half ** 2 * n) % MOD

def inverse(n):
    return pow(factorial[n], MOD-2)

MOD = 1000000007
factorial = [1] * 4000001
for idx in range(2, 4000001):
    factorial[idx] = (factorial[idx-1] * idx) % MOD

m = int(input())
for _ in range(m):
    n, k = map(int, stdin.readline().split())
    stdout.write(str((factorial[n] * inverse(n-k) * inverse(k)) % MOD))
    stdout.write('\n')
stdout.flush()