import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
n = int(input())
nums = list(map(int, input().split()))
count = defaultdict(int)
for i in range(n):
    count[nums[i]] += 1
    if len(count) > N:
        min_val = float('inf')
        for candidate in count:
            if candidate == nums[i]:
                continue
            if count[candidate] < min_val:
                min_val = count[candidate]
                target = candidate
        del count[target]
answer = []
for candidate in count:
    answer.append(candidate)
print(*sorted(answer))