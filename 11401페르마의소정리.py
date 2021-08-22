def pow(n, k, m):
    if k == 1:
        return n
    pow_half = pow(n, k//2, m)
    if k % 2 == 0:
        return (pow_half ** 2) % m
    else:
        return (pow_half ** 2 * n) % m

n, k = map(int, input().split())

factorial = [1] * (n+1)
for idx in range(2, n+1):
    factorial[idx] = (factorial[idx-1] * idx) % 1000000007

def inverse(n):
    return pow(factorial[n], 1000000005, 1000000007)

print(factorial[n] * inverse(n-k) * inverse(k) % 1000000007)