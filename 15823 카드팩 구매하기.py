import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.append(cards[-1])

# 연속된 카드 묶기. 정확히 M개의 카드팩. 같은 종류 카드 두장되면 안됨.
# 카드팩의 최대 길이.
left = 0
pack_cnt = []
card_pack = defaultdict(int)
for right in range(N+1):
    card_pack[cards[right]] += 1
    if card_pack[cards[right]] > 1:
        pack_cnt.append(right-left)
    while card_pack[cards[right]] > 1:
        card_pack[cards[left]] -= 1
        left += 1

pack_cnt.sort(reverse=True)
for i in range(max(pack_cnt),1,-1):
    max_cnt = 0
    for cnt in pack_cnt:
        max_cnt += cnt//i
    if max_cnt >= M:
        print(i)
        exit()
else:
    print(1)