import sys
input  = sys.stdin.readline
from itertools import combinations


while 1:
    k_lists = list(map(int,input().split()))
    k = k_lists[0] 

    if k ==0:
        break
    
    coms = combinations(k_lists[1:],6)

    for nums in coms:
        print(*nums)
    print("")