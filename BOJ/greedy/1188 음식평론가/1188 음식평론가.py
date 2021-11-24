def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)
n, m = map(int, input().split())
print(m - GCD(n, m))