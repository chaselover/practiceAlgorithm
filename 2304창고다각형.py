import sys
input = sys.stdin.readline

N = int(input())
pillars = [list(map(int, input().split())) for _ in range(N)]
pillars.sort()
height = 0
left = 0
answer = 0
for pillar in pillars:
    if height <= pillar[1]:
        answer += (pillar[0] - left)*height
        height = pillar[1]
        left = pillar[0]
height = 0
left = 0
pillars.reverse()
for pillar in pillars:
    if height <= pillar[1]:
        answer += (left - pillar[0])*height
        height = pillar[1]
        left = pillar[0]
left = 0
h_t = 0
for pillar in pillars:
    if height == pillar[1]:
        answer -= (left - pillar[0])*h_t
        left = pillar[0]
        h_t = pillar[1]
answer += height
print(answer)