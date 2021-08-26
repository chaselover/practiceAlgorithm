import sys
input = sys.stdin.readline
from math import ceil

h_hp, h_atk, d_hp, d_atk = map(int, input().split())
P, S = map(int, input().split())
# h_hp d_atk로 나눈 몫 올림값이 용사 사망 cnt
h_death_cnt = ceil(h_hp/d_atk)
# d_hp - P 를 h_atk로 때린 나머지에 P를 더한 값이 h_atk보다 작을경우 d_hp - P를 h_atk로 나눈 몫+1에 끔살
if (d_hp-P)%h_atk and (d_hp-P)%h_atk + P <= h_atk:
    d_death_cnt = ceil(d_hp/h_atk)
else:
    # 클 경우 한대더맞고 S회복하고 다시 때려서 cnt 계산
    d_death_cnt = ceil((d_hp+S)/h_atk)

# 세개 비교해서 승패 비교.
if h_death_cnt >= d_death_cnt:
    print('Victory!')
else:
    print('gg')