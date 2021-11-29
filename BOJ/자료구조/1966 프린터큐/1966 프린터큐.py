import sys
read = sys.stdin.readline
f = lambda: map(int, read().split())

for _ in range(int(read())):
    n,m = f()
    s = [*f()]
    num = s[m]
    s.reverse()

    cnt, target = 0,0
    for i in range(9,num,-1):
        cnt += s.count(i)
        try:
            target = s.index(i,target,n)
        except ValueError:
            try:
                target = s.index(i,0,target+1)
            except ValueError:
                pass
    m = -m + n -1

    if target <= m:
        print(s[0:target].count(num) + s[m::].count(num) + cnt)
    else:
        print(s[m:target].count(num) + cnt)
