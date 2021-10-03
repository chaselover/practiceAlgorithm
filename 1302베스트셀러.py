import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
sell = defaultdict(int)
for __ in range(N):
    book = input().rstrip()
    sell[book] += 1

arr_for_sort = []
for book in sell:
    arr_for_sort.append((sell[book], str(book)))

arr_for_sort.sort(key=lambda x: (-x[0], x[1]))
print(arr_for_sort[0][1])