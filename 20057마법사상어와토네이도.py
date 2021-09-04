import sys
input = sys.stdin.readline

def spread_sand(x,y,d):
    total_sand = A[x][y]
    out_sand = 0
    A[x][y] = 0
    try:
        A[x+d][y+d] += int(total_sand*0.55)
    except:
        out_sand += int(total_sand*0.55)



def move(x,y,d,cnt,flag,sand):
    if not x and not y:
        print(sand)
        exit()
    for _ in range(cnt):
        x += d_tor[d][0]
        y += d_tor[d][1]
        out_sand = spread_sand(x,y,d)
    if flag:
        flag ^= 1
        cnt += 1
    else:
        flag ^= 1
    move(x,y,(d+1)%4,cnt,flag,sand+out_sand)
    


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
# 토네이도는 matrix가운데부터 이동.
# 토네이도가 이동한 칸의 모든 모래가 비율대로 흩어진다.(소숫점 아래는 버린다) - 총량에서 남은 모든 양은 a로 55퍼.
# 토네이도는 1,1까지 이동 후 소멸.(N은 홀수.) / 가운데 칸 모래는 0으로 시작.
# 격자 밖으로 나간 모래의 양을 출력.
start_x, start_y = N//2, N//2
cnt = 1
# (0,-1), (1,0) 각 cnt번 이동 후 cnt += 1
# (0,1), (-1,0) 각 cnt번 이동 후 cnt += 1
d_tor = [(0,-1),(1,0),(0,1),(-1,0)]
sand_ratio = [0.55,0.05,0.1,0.1,0.07,0.07,0.02,0.02,0.01,0.01]
move(start_x,start_y,0,1,0,0)