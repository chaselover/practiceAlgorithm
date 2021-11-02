import sys
import itertools
input = sys.stdin.readline

a, b = input().split()
b = int(b)
lst = list(map(''.join, list(itertools.permutations(a))))
c = -1
for num in lst:
    first = num[0]
    num = int(num)
    if b >= num and first != '0':
        c = max(c, num)
print(c)