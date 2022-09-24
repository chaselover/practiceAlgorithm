import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
cards = list(map(int, input().split()))

LIS = [0]
for card in cards:
    if card > LIS[-1]:
        LIS.append(card)
    else:
        LIS[bisect_left(LIS,card)] = card
print(len(LIS)-1)