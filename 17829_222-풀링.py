import sys
input = sys.stdin.readline

def polling(n,start_x,start_y):
    half = n//2
    if n==2:
        arr = [matrix[start_x][start_y], matrix[start_x+1][start_y], matrix[start_x][start_y+1], matrix[start_x+1][start_y+1]]
        arr.sort()
        return arr[-2]
    left_top = polling(half,start_x,start_y)
    right_top = polling(half,start_x+half,start_y)
    left_bottom = polling(half,start_x,start_y+half)
    right_bottom = polling(half,start_x+half,start_y+half)
    arr = [left_top, right_top, left_bottom, right_bottom]
    arr.sort()
    return arr[-2]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(polling(N,0,0))
