def check(b,n):
    c.add(tuple(b))
    for i in range(1,n):
        if b[i] == b[i-1]:
            tmp = b[:i-1] + [b[i]+b[i-1]] + b[i+1:]
            check(tmp,n-1)


def solution(a, s):
    results = []
    bs = []
    idx = 0
    s_cnt = len(s)
    for n in s:
        bs.append(a[idx:idx+n])
        idx = idx+n
    for i  in range(s_cnt):
        global c
        b = bs[i]
        n = s[i]
        c = set()
        check(b,n)
        results.append(len(c))
    return results

print(solution([1,2,3,4,5,6,7,8,9],[2,3,4]))