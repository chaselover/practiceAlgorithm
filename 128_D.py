n, k = map(int, input().split())
n += 1
a = list(map(int, input().split()))
a.insert(0, 0)
p, q = [0]*n, [0]*n

for i in range(1, n):
    p[i], q[i] = p[i-1] + (a[i] == 0), q[i-1] + a[i]

s, r = q[n-1], -1
for t in range(2):
    for i in range(n):
        for j in range(i+1, n):
            c = p[j]-p[i]
            x = p[n-1]-c
            v = 0
            if t == 0:
                v = max(-c*k, min(c*k, x*k-s))
            else:
                v = min(c*k, max(-c*k, -s-x*k))
            if s-x*k+v <= 0 and 0 <= s+x*k+v:
                r = max(r, 1 + abs(q[j] - q[i] + v))
print(r)