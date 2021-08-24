n = int(input())
f = sorted(list(map(float, input().split())))
c = 0
for i in range(n):
    l = i
    r = n
    while l < r:
        m = (l+r)//2
        if f[i]>=(0.9)*f[m]:
            l = m + 1
        else:
            r = m
    c += r-i-1
print(c)
