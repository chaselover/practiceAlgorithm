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



# # 남의코드 가로세로만 바뀜.
# import sys
# input = sys.stdin.readline

# s = input().rstrip()
# d = [[0] * 26 for _ in range(len(s) + 1)]

# for i in range(1, len(s) + 1):
#     x = ord(s[i - 1]) - ord("a")
#     for j in range(26):
#         if j == x:
#             d[i][j] = d[i - 1][j] + 1
#             continue
#         d[i][j] = d[i - 1][j]

# n = int(input())
# for _ in range(n):
#     x, l, r = input().rstrip().split()
#     x = ord(x) - ord("a")
#     r = int(r)
#     l = int(l)

#     ans = d[r + 1][x] - d[l][x]
#     sys.stdout.write(str(ans) + "\n")