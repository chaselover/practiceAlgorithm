import sys
input = sys.stdin.readline

N = int(input())
h = list(map(int,input().split()))

two = 0
one = 0
for wood in h:
    two += wood//2
    one += wood%2

if not (two-one)%3 and two >= one:
    print('YES')
else:
    print('NO')