import sys
import math
input = sys.stdin.readline

n = int(input())

coord_list = []
for _ in range(n):
    x, y = map(int, input().split())
    coord_list.append((x, y))

coord_list.append(coord_list[0])		#(x1, y1) 좌표를 coord_list 마지막에 다시 추가

plus = 0	
minus = 0
for i in range(len(coord_list) - 1):
    plus += (coord_list[i][0] * coord_list[i+1][1])
    minus += (coord_list[i][1] * coord_list[i+1][0])
    # fabs는 소숫점 있는 수의 절댓값(abs는 정수)
area = math.fabs(0.5 * (plus - minus))
print("%.1f" % area)