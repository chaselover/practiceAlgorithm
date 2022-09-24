import sys
from collections import Counter
input = sys.stdin.readline

def triangle_area(tri):
    y_list = [tri[0][1], tri[1][1], tri[2][1]]
    x_list = [tri[0][0], tri[1][0], tri[2][0]]
    height = max(y_list) - min(y_list)
    width = max(x_list) - min(x_list)
    return height * width / 2
    
n,m = map(int,input().split())

matrix = [list(input().rstrip()) for _ in range(n)]
counter = {'R': 0, 'G':0 , 'B':0}
for i in range(n):
    A = list(Counter(matrix[i]).items())
    for colors in A:
        key,value = colors
        counter[key] += value

max_cnt = 1
for color in 'RGB':
    max_cnt*=counter[color]

for i in range(n):
    for j in range(m):
