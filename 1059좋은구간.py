import sys
input = sys.stdin.readline
from bisect import bisect

L = int(input())
AB_list = list(map(int,input().split()))
AB_list.sort()
N = int(input())
if N < AB_list[0]:
    answer = max(0,(AB_list[0]-N)*(N)-1)
else:
    index= bisect(AB_list,N)
    answer = max(0,(AB_list[index]-N)*(N-AB_list[index-1])-1)
print(answer)