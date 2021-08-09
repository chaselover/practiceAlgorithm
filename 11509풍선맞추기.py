import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int,input().split()))
arrows = []
for i in range(N):
    if H[i]+1 in arrows:
        arrows[arrows.index(H[i]+1)] -=1
    else:
        arrows.append(H[i])

print(len(arrows))

# 다른풀이
# n = int(input())
# l = [int(i) for i in input().split()]
# h_l = [0] * 1000001
# arrow = 0

# for i in l:
#     if h_l[i]:
#         h_l[i] -= 1
#         h_l[i - 1] += 1
#     else:
#         arrow += 1
#         h_l[i - 1] += 1

# print(arrow)
