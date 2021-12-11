
import sys
input = sys.stdin.readline
from collections import defaultdict
 
 
for test in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = defaultdict(int)
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            cnt[arr[i]] += 1
    if not cnt:
        print(0)
        continue
    if arr[0] not in cnt:
        print(1)
        continue
    min_value = min(cnt.values())
    if min_value != cnt[arr[-1]]:
        min_value += 1
    print(min_value)