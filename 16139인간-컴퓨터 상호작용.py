import sys
input = sys.stdin.readline
print = sys.stdout.write

s = input().rstrip()
n = len(s)
sub_set = [[0 for _ in range(26)] for _ in range(n)]
for i in range(n):
    for j in range(i,n):
        sub_set[j][ord(s[i])-97] += 1

q = int(input())
for _ in range(q):
    alp, l, r = input().split()
    l,r = int(l), int(r)
    l_value = sub_set[l-1][ord(alp)-97] if l>0 else 0
    r_value = sub_set[r][ord(alp)-97]
    print(f'{r_value - l_value}\n')
