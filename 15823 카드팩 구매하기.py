import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 연속된 카드 묶기. 정확히 M개의 카드팩. 같은 종류 카드 두장되면 안됨.
# 카드팩의 최대 길이.
left = 0
max_cnt = 0
card_pack = defaultdict(int)
for right in range(N):
    card_pack[cards[right]] += 1
    if card_pack[cards[right]] > 1:
        max_cnt = max(max_cnt,right-left)
    while card_pack[cards[right]] > 1:
        card_pack[cards[left]] -= 1
        left += 1
print(max_cnt)