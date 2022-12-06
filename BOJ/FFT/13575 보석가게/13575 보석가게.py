def power(a, b, mod):
    result = 1
    while b:
        if b % 2:
            result *= a
            result %= mod
        b //= 2
        a *= a
        a %= mod
    return result


def fft(a, inv=False):
    n = len(a)
    y = 0
    for x in range(1, n):
        rev = n // 2
        while y >= rev:
            y -= rev
            rev //= 2
        y += rev
        if x < y:
            a[x], a[y] = a[y], a[x]
    step = 2
    while step <= n:
        half = step // 2
        u = power(3, div // step, div)
        if inv:
            u = power(u, div - 2, div)
        for x in range(0, n, step):
            w = 1
            for y in range(x, x + half):
                v = a[y + half] * w
                a[y + half] = (a[y] - v) % div
                a[y] += v
                a[y] %= div
                w *= u
                w %= div
        step *= 2
    if inv:
        c = div - (div - 1) // n
        for idx in range(n):
            a[idx] = (a[idx] * c) % div


div = 469762049
nn = 1 << 20
arr = [0] * nn
n, k = map(int, input().split())
for i in map(int, input().split()):
    arr[i] = 1
k -= 1
fft(arr)
ans = arr[:]
while k:
    if k % 2:
        for i in range(nn):
            ans[i] *= arr[i]
            ans[i] %= div
    k //= 2
    for i in range(nn):
        arr[i] *= arr[i]
        arr[i] %= div
fft(ans, inv=True)
res = []
for i in range(1, nn):
    if ans[i]:
        res.append(i)
print(*res)
