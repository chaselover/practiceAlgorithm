from math import gcd

for i in range(int(input())):
    a,b = map(int,input().split())
    g = gcd(a,b)
    print(a*b//g)