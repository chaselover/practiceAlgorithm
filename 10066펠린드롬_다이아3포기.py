import sys
input = sys.stdin.readline
from collections import defaultdict

def manacher(s):
    cnt = defaultdict(int)
    n = len(s)
    P = [0]*n
    c = 0
    r = 0

    for i in range(n):

        if i > r:
            P[i] = 0
        else:
            P[i] = min(P[2*c-i],r-i)
            cnt[s[i-P[i]:i+P[i]+1]] += 1
        while i-P[i]-1 > 0 and i+P[i]+1 < n and s[i+P[i]+1] == s[i-P[i]-1]:
            P[i] += 1
            cnt[s[i-P[i]:i+P[i]+1]] += 1
        if r < i + P[i]:
            r = i + P[i]
            c = i
    return cnt

st = input().rstrip()
cnt_table = manacher('#' + '#'.join(st) + '#')
max_value = 0
for p in cnt_table:
    if p == '#':
        continue
    if p[0]!='#':
        max_value = max(max_value,(len(p)//2+1)*cnt_table[p])
    else:
        max_value = max(max_value,(len(p)//2)*cnt_table[p])
print(max_value)