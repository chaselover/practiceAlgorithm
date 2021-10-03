import sys
input = sys.stdin.readline
from collections import defaultdict
from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
check = defaultdict(int)
nums = set()
for num in arr:
    check[num] += 1
    nums.add(num)
answer = 0
for num in nums:
    if (x - num) in check:
        if 2 * num == x:
            answer += len(list(combinations([i for i in range(check[num])], 2)))
            continue
        answer += check[num] * check[x - num]
        del check[num]
        del check[x - num]
print(answer)