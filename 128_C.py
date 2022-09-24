for _ in range(int(input())):
    s = input().strip().strip('0')
    z = s.count('0')
    a = list(map(len, s.split('1')))[1:-1]
    best, r, sm, n = z, 0, 0, len(a)
    for l in range(len(a)):
        while r < n and sm + a[r] <= n - r + l:
            sm += a[r]
            r += 1
        best = min(best, max(sm, n - r + l))
        sm -= a[l]
    print(best)