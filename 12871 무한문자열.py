import sys
input = sys.stdin.readline
from math import gcd

s = input().rstrip()
t = input().rstrip()
n = len(s)
m = len(t)
a = gcd(n,m)
if s*(m//a) == t*(n//a):
    print(1)
else:
    print(0)