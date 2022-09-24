import sys
input = sys.stdin.readline

def manacher(s):
    n = len(s)
    P = [0]*n
    c = 0
    r = 0

    for i in range(n):

        if i > r:
            P[i] = 0
        else:
            P[i] = min(P[2*c-i],r-i)
        while i-P[i]-1 > 0 and i+P[i]+1 < n and s[i+P[i]+1] == s[i-P[i]-1]:
            P[i] += 1
        if r < i + P[i]:
            r = i + P[i]
            c = i
    return P

st = input().rstrip()
a_table = manacher('#' + '#'.join(st) + '#')
M = int(input())
for _ in range(M):
    start, length = map(int, input().split())
    cnt = 0
    for i in range(len(a_table)):
        if a_table[i] >= length and i - a_table[i] == start*2+1:
            cnt += 1
    print(cnt)
