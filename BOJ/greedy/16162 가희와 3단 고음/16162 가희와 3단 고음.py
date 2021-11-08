n, a, d = map(int,input().split())
L = list(map(int,input().split()))
check = 0
for pt in range(n):
    if L[pt] == a:
        check += 1
        a += d
print(check)