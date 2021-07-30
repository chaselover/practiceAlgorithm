import sys
import math

input = lambda: sys.stdin.readline().rstrip()

N, A, B, C, D = map(int, input().split())

def compare(a, b, c, d):
    if (a/b) > (c/d):
        return a, b, c, d
    else:
        return c, d, a, b

an, bn, cn, dn = compare(A, B, C, D)

compare_min = float('inf')

for flower1 in range(an):
    flower2 = math.ceil((N - flower1 * cn)/an)
    price1 = flower1 * dn 
    price2 = flower2 * bn

    if price2<0: price2 = 0
    
    compare_min = min(compare_min, price1+price2)

print(compare_min)